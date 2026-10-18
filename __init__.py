"""仅用于依赖版本冲突演示的 ComfyUI 文本节点。"""


class KKMistuneLegacy:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "文本": ("STRING", {
                    "multiline": True,
                    "default": "你好，**ComfyUI**！",
                }),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("HTML文本", "依赖版本")
    FUNCTION = "convert"
    CATEGORY = "KK测试/依赖版本冲突"
    OUTPUT_NODE = True
    DESCRIPTION = "使用 Mistune 0.8.4 将 Markdown 文本转换为 HTML。"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        # 演示节点每次排队均执行，以便观察实际依赖及结果。
        return float("nan")

    def convert(self, 文本):
        # 执行时才导入及调用版本相关接口，不在注册节点时调用。
        import mistune

        renderer = mistune.Renderer(escape=True)
        markdown = mistune.Markdown(renderer=renderer)
        html = str(markdown(文本))
        version = str(mistune.__version__)
        report = "实际依赖：mistune " + version + "\n\n转换结果：\n" + html
        return {
            "ui": {"text": [report]},
            "result": (html, version),
        }


NODE_CLASS_MAPPINGS = {"KKMistuneLegacy": KKMistuneLegacy}
NODE_DISPLAY_NAME_MAPPINGS = {"KKMistuneLegacy": "旧版文本转换（Mistune 0.8.4）"}
WEB_DIRECTORY = "./web"
