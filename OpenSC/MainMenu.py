import pygame
import random
import os
import math
class MainMenu():
    def __init__(self):
        # Inits
        pygame.init()
        pygame.display.init()
        pygame.font.init()
        pygame.mixer.init()
        # Fonts
        self.Arial = pygame.font.SysFont('Arial', 30)
        self.MadeOriginal1 = self.Arial.render("the original game on which it was", False, (50,50,50))
        self.MadeOriginal2 = self.Arial.render("\"based\" was made by Candy Rufus Games", False, (50,50,50))
        self.InitVars()
        self.ImagesLoad()
        self.CreateDisplay()
        self.SplashMainLoop()
        self.MenuButtons()
        self.MenuMainLoop()
    def CreateDisplay(self):
        self.ScreenSize = (1024, 720)
        self.ScreenCenterX, self.ScreenCenterY = self.ScreenSize[0]//2, self.ScreenSize[1]//2
        self.Display = pygame.display.set_mode(self.ScreenSize, pygame.FULLSCREEN)
    def GetCenterScreen(self, Image):
        return (self.ScreenCenterX - Image.get_width()//2, self.ScreenCenterY - Image.get_height()//2)
    def ImagesLoad(self):
        self.Panorama = pygame.image.load(self.GuiImages + "Panorama.png")
        self.Logo = pygame.image.load(self.GuiImages + "Logo.png")
        
        self.CandyRufusGames = pygame.image.load(self.GuiImages + "CandyRufusLogo.png")
    def SplashMainLoop(self):
        Clock = pygame.time.Clock()
        # Intro MainLoop
        while 1:
            Clock.tick(30)
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if ev.type == pygame.KEYUP:
                    if ev.key == pygame.K_q:
                        pygame.quit()
                        exit()
            self.Display.fill((255, 255,255))
            self.Display.blit(self.CandyRufusGames, self.GetCenterScreen(self.CandyRufusGames))
            self.Display.blit(self.MadeOriginal1, (0,self.ScreenSize[1]-60))
            self.Display.blit(self.MadeOriginal2, (0,self.ScreenSize[1]-30))
            now = pygame.time.get_ticks()
            if now >= 2000:
                self.Display.fill((0,0,0))
                pygame.display.flip()
                break
            pygame.display.flip()
    def InitVars(self):
        self.MusicsList = os.listdir("appearance/Content/Music")
        self.GuiImages = "appearance/Content/Textures/Gui/"
    def MenuButtons(self):
        ButtonBackground = pygame.Surface((300, 80))
        ButtonBackground.fill((100,100,100))

        Play = ButtonBackground.copy()
        PlayText = self.Arial.render("Play", False, (255,255,255))
        Play.blit(PlayText, (Play.get_width()//2-PlayText.get_width()//2, Play.get_height()//2-PlayText.get_height()//2))


        Community = ButtonBackground.copy()
        CommunityText = self.Arial.render("Content", False, (255,255,255))
        Community.blit(CommunityText, (Community.get_width()//2-CommunityText.get_width()//2, Community.get_height()//2-CommunityText.get_height()//2))
        self.Play = Play
        self.ButtonBackground = ButtonBackground
        self.Content = Community
    def MenuMainLoop(self):
        pygame.mixer.music.load("appearance/Content/Music/" + random.choice(self.MusicsList))
        pygame.mixer.music.play()
        ######################
        Clock = pygame.time.Clock()
        PanoramaX = -250
        PanoramaY = -250
        Zoom = 0
        LogoZoomDirection = "Zoom"
        LogoZoom = 0
        LogoZoomUnround = 0
        ChunkSize = 16
        PanoramaSize = (self.ScreenSize[0] * 2, self.ScreenSize[1] * 2)
        while 1: # Menu Main Loop
            self.Display.fill((0,0,0))
            dt = Clock.tick(30)
            
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if ev.type == pygame.KEYUP:
                    if ev.key == pygame.K_q:
                        pygame.quit()
                        exit()
            
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load("appearance/Content/Music/" + random.choice(MusicsList))
                pygame.mixer.music.play()
            
            if LogoZoomDirection == "Zoom":
                LogoZoomUnround += 0.25
                if LogoZoomUnround >= 10:
                    LogoZoomDirection = "Unzoom"
            elif LogoZoomDirection == "Unzoom":
                LogoZoomUnround -= 0.25
                if LogoZoomUnround <= 0:
                    LogoZoomDirection = "Zoom"
            LogoZoom = math.ceil(LogoZoomUnround)
            
            
            
            self.Display.blit(pygame.transform.scale(self.Logo, (self.Logo.get_width()+LogoZoom, self.Logo.get_height()+LogoZoom-Zoom)), (self.ScreenSize[0]//2-self.Logo.get_width()//2-LogoZoom, self.ScreenSize[1]//4-self.Logo.get_height()//2-LogoZoom))
            self.Display.blit(self.Play, (self.ScreenSize[0]//2.80-self.Play.get_width()//2, self.ScreenCenterY))
            self.Display.blit(self.Content, (self.ScreenSize[0]//1.50-self.Play.get_width()//2, self.ScreenCenterY))
            #self.Display.blit(pygame.transform.scale(Panorama, (PanoramaSize[0]+Zoom, PanoramaSize[1]+Zoom)), (PanoramaX, PanoramaY))
            pygame.display.flip()



MainMenu()


