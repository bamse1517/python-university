import pygame

class Paddle(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    super().__init__()

    self.image = pygame.Surface([width, height])
    self.image.fill([0,0,0])
    self.image.set_colorkey([0,0,0])

    # 사각형 막대 그리기
    pygame.draw.rect(self.image, color, [0,0,width, height])
    self.rect = self.image.get_rect()

  def move_up(self, pixels):
    self.rect.y -= pixels
    if self.rect.y < 0:
      self.rect.y = 0

  def move_down(self, pixels):
    self.rect.y += pixels
    if self.rect.y > 400:
      self.rect.y = 400