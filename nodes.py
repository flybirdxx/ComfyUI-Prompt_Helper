import folder_paths
import os

try:
    from llama_cpp import Llama
    LLAMA_CPP_AVAILABLE = True
except ImportError:
    LLAMA_CPP_AVAILABLE = False
    print("\033[31m[Qwen Node Error] llama-cpp-python 未安装！无法加载 GGUF 模型。请运行: pip install llama-cpp-python\033[0m")



class Qwen3Engineer:
    _model_cache = {}
    
    @classmethod
    def INPUT_TYPES(s):
        file_list = []
        text_encoder_paths = folder_paths.get_folder_paths("text_encoders")
        for path in text_encoder_paths:
            if os.path.exists(path):
                for root, dirs, files in os.walk(path):
                    for file in files:
                        if file.lower().endswith('.gguf'):
                            rel_path = os.path.relpath(os.path.join(root, file), path)
                            file_list.append(rel_path.replace(os.sep, '/'))
        
        if not file_list:
            file_list = ["Put_GGUF_in_models/text_encoders_folder.gguf"]

        return {
            "required": {
                "gguf_name": (file_list, ),
                "system_prompt": ("STRING", {
                    "default": """You are Z-Engineer, an expert prompt engineering AI specializing in the Z-Image Turbo architecture (S3-DiT). Your goal is to rewrite simple user inputs into high-fidelity, "Positive Constraint" prompts optimized for the Qwen-3 text encoder and the 8-step distilled inference process.

**CORE OPERATIONAL RULES:**
1.  **NO Negative Prompts:** Z-Image Turbo ignores negative prompts at the optimal CFG of 1.0. You must strictly use "Positive Constraints." (e.g., instead of "negative: blur", write "...razor sharp focus, pristine imaging...").
2.  **Natural Language Syntax:** The Qwen-3 encoder requires coherent, grammatical sentences. Do NOT use "tag salad" (comma-separated lists). Use flow and structure.
3.  **Texture Density:** The model suffers from "plastic skin" unless forced to render high-frequency detail. You must aggressively describe textures (e.g., "weathered skin," "visible pores," "film grain," "fabric weave") to engage the "Shift 7.0" sampling schedule.
4.  **Spatial Precision:** Use specific spatial prepositions ("in the foreground," "to the left," "worm's-eye view") to leverage the 3D RoPE embeddings.
5.  **Text Handling:** If the user asks for text/signage, explicitly enclose the text in double quotes (e.g., ...a sign that says "OPEN"...) and describe the font/material (e.g., "neon," "stenciled paint").
6. **Proper Anatomy:** If the user asks for a living subject (e.g., an animal or person), explicitly state that they have proper anatomy or "perfectly formed" is used when describing the subject (e.g., "The woman's perfectly formed hands hold".
7. **Camera & Lens:** Unless specified by the user choose a camera and lens type that suits the style. (e.g. for a portrait, Nikon D850 with 50mm f/1.4 lens). ALWAYS explicitly use the words "shot on" or "shot with" when describing the camera type (e.g. "A beautiful portrait of a woman shot on a Nikon D850 with 50mm f/1.4 lens, shallow depth of field").

**PROMPT STRUCTURE HIERARCHY:**
Construct your response in this specific order:
1.  **Subject Anchoring:** Define the WHO and WHAT immediately.
2.  **Action & Context:** Define the DOING and WHERE.
3.  **Aesthetic & Lighting:** Define the HOW (Lighting, Atmosphere, Color Palette).
4.  **Technical Modifiers:** Define the CAMERA (Lens, Film Stock, Resolution).
5.  **Positive Constraints:** Define the QUALITY (e.g., "clean background," "architectural perfection," "proper anatomy," "perfectly formed").

**OUTPUT FORMAT:**
Return ONLY the enhanced prompt string, followed by a brief "Technical Metadata" block.

**Example Input:**
"A photo of an old man."

**Example Output:**
An extreme close-up portrait of an elderly fisherman with deep weathered skin and salt-and-pepper stubble, wearing a yellow waterproof jacket. He is standing against a dark stormy ocean background with raindrops on his face. The lighting is dramatic and side-lit, emphasizing the texture of his skin. Shot on an 85mm lens at f/1.8 with Fujifilm Superia 400 film stock, featuring high texture, raw photo quality, and visible film grain.

[Technical Metadata]
Steps: 8
CFG: 1.0
Sampler: Euler
Schedule: Simple
Shift: 7.0 (Crucial for skin texture)""", 
                    "multiline": True
                }),
                "prompt": ("STRING", {
                    "default": "Generate a detailed prompt.", 
                    "multiline": True
                }),
                "n_ctx": ("INT", {"default": 4096, "min": 2048, "max": 32768, "tooltip": "上下文窗口大小"}),
                "n_gpu_layers": ("INT", {"default": -1, "min": -1, "max": 100, "tooltip": "-1 表示将所有层加载到 GPU (推荐)"}),
                "max_new_tokens": ("INT", {"default": 512, "min": 16, "max": 4096}),
                "temperature": ("FLOAT", {"default": 0.7, "min": 0.0, "max": 1.0, "step": 0.01}),
                "seed": ("INT", {"default": -1, "min": -1, "max": 2147483647, "tooltip": "随机种子，-1 表示使用随机种子"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "generate"
    CATEGORY = "QwenTextEngineer"

    def load_gguf(self, gguf_name, n_ctx, n_gpu_layers):
        cache_key = f"{gguf_name}_{n_ctx}_{n_gpu_layers}"
        if cache_key in self._model_cache:
            return self._model_cache[cache_key]

        if not LLAMA_CPP_AVAILABLE:
            raise Exception("缺少 llama-cpp-python 库。请在终端运行: pip install llama-cpp-python")

        gguf_path = folder_paths.get_full_path("text_encoders", gguf_name)
        if not gguf_path:
            text_encoder_paths = folder_paths.get_folder_paths("text_encoders")
            for path in text_encoder_paths:
                if os.path.exists(path):
                    full_path = os.path.join(path, gguf_name)
                    if os.path.isfile(full_path):
                        gguf_path = full_path
                        break
        
        if not gguf_path or not os.path.isfile(gguf_path):
            raise FileNotFoundError(f"在 models/text_encoders 中找不到文件: {gguf_name}")

        print(f"Loading GGUF model from: {gguf_path}...")
        
        try:
            llm = Llama(
                model_path=gguf_path,
                n_ctx=n_ctx,
                n_gpu_layers=n_gpu_layers,
                verbose=True,
                logits_all=True
            )
            
            print("GGUF Model loaded successfully!")
            self._model_cache[cache_key] = llm
            return llm

        except Exception as e:
            print(f"Error loading GGUF model: {e}")
            raise e

    def generate(self, gguf_name, system_prompt, prompt, n_ctx, n_gpu_layers, max_new_tokens, temperature, seed):
        llm = self.load_gguf(gguf_name, n_ctx, n_gpu_layers)
        
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        try:
            completion_params = {
                "messages": messages,
                "max_tokens": max_new_tokens,
                "temperature": temperature,
            }
            
            # 只有当 seed >= 0 时才设置 seed 参数
            if seed >= 0:
                completion_params["seed"] = seed
            
            response = llm.create_chat_completion(**completion_params)
            output_text = response["choices"][0]["message"]["content"]
            return (output_text,)
        except Exception as e:
            return (f"Error during GGUF generation: {e}",)


NODE_CLASS_MAPPINGS = {
    "QwenImageEngineer": Qwen3Engineer
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "QwenImageEngineer": "Qwen3 Engineer"
}
