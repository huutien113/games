import pygame
import sys

# Khởi tạo pygame
pygame.init()

# Khai báo kích thước cửa sổ game
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load ảnh
background = pygame.image.load("background.png")
player = pygame.image.load("player.png")
key = pygame.image.load("key.png")
door = pygame.image.load("door.png")

# Thiết lập vị trí ban đầu của nhân vật và chìa khóa
player_x = 100
player_y = 100
key_x = 400
key_y = 300

# Thiết lập vị trí của cửa và trạng thái của nó
door_x = 0
door_y = 0
door_locked = True

# Vòng lặp game
while True:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Vẽ ảnh nền
    screen.blit(background, (0, 0))

    # Vẽ nhân vật và chìa khóa
    screen.blit(player, (player_x, player_y))
    screen.blit(key, (key_x, key_y))

    # Kiểm tra va chạm giữa nhân vật và chìa khóa
    if player_x == key_x and player_y == key_y:
        # Nếu va chạm xảy ra, mở cửa
        door_locked = False

    # Kiểm tra trạng thái của cửa
    if door_locked:
        # Nếu cửa bị khóa, vẽ cửa khóa
        screen.blit(door, (door_x, door_y))
    else:
        # Nếu cửa được mở, thoát khỏi mê cung
        sys.exit()

    # Cập nhật màn hình
    pygame.display.update()
