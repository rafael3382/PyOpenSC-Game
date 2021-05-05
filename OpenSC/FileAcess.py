class BasicsConfigs:
        def __init__(self):
            self.Configs={
                "Resolution": [800, 800],
                "Graphics": "Medium",
                "Shader": "Default",
                "VisibilityRange": 112,
                "DefaultTexture": "Default",
                "Controls": "Arrows",
                "BlockAddon": None,
                "DefaultPlayer": "Default"
                "MessageStyleMinecraft": False,
                "SkyRender": "Full&Realist",
                "FramerateLimit": 60,
                "WorldMaker": "Default",
                "CircuitSpeed": 0.0001,
                "time_speed": "10Minute",
                "EletricityVoltages": "0123456789ABCDEF",
            }
            self.Texture = None
            self.GameFolder = os.path.abspath(__file__)
        def ResetTexture(self):
            self.Texture = self.Config[DefaultTexture]
