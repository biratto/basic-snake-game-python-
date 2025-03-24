import pygame
import random

pygame.init()

# Ekran boyutları
ekran_genişlik = 1200
ekran_yükseklik = 800
ekran = pygame.display.set_mode((ekran_genişlik, ekran_yükseklik))

# Oyun başlığı
pygame.display.set_caption("Snake")

# Yılanın başlangıç pozisyonu
yilan = [(300, 200), (290, 200), (280, 200)]
yilan_hizi = 10

# Yiyeceğin başlangıç pozisyonu
yiyecek = (random.randrange(0, ekran_genişlik, yilan_hizi), random.randrange(0, ekran_yükseklik, yilan_hizi))

# Oyun hızı ayarı
clock = pygame.time.Clock()

# Puan
puan = 0

# Yılanın başlangıç yönü
yön = "RIGHT"

# Oyun döngüsü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Yön değişikliği
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and yön != "RIGHT":
                yön = "LEFT"
            elif event.key == pygame.K_RIGHT and yön != "LEFT":
                yön = "RIGHT"
            elif event.key == pygame.K_UP and yön != "DOWN":
                yön = "UP"
            elif event.key == pygame.K_DOWN and yön != "UP":
                yön = "DOWN"

    # Yılanın hareketi
    if yön == "RIGHT":
        yeni_kafa = (yilan[0][0] + yilan_hizi, yilan[0][1])
    elif yön == "LEFT":
        yeni_kafa = (yilan[0][0] - yilan_hizi, yilan[0][1])  # Düzeltme: yilan[0][0] yanlış kullanılmış
    elif yön == "UP":
        yeni_kafa = (yilan[0][0], yilan[0][1] - yilan_hizi)
    elif yön == "DOWN":
        yeni_kafa = (yilan[0][0], yilan[0][1] + yilan_hizi)

    # Yılanın başını ekliyoruz
    yilan.insert(0, yeni_kafa)

    # Yılan yiyeceği yedi mi?
    if yilan[0] == yiyecek:
        yiyecek = (random.randrange(0, ekran_genişlik, yilan_hizi), random.randrange(0, ekran_yükseklik, yilan_hizi))
        puan += 10  # Puanı artırıyoruz
    else:
        yilan.pop()  # Yılanın son segmentini çıkarıyoruz

    # Yılanın kendisine çarpması
    if yilan[0] in yilan[1:]:
        pygame.quit()
        quit()

    # Ekran sınırlarına çarpma
    if yilan[0][0] >= ekran_genişlik or yilan[0][1] >= ekran_yükseklik or yilan[0][0] < 0 or yilan[0][1] < 0:
        pygame.quit()
        quit()

    # Ekranı siyah renge boyama
    ekran.fill((0, 0, 0))

    # Yılanı çizme
    for segment in yilan:
        pygame.draw.rect(ekran, (0, 255, 0), (segment[0], segment[1], yilan_hizi, yilan_hizi))

    # Yiyeceği çizme
    pygame.draw.rect(ekran, (255, 0, 0), (yiyecek[0], yiyecek[1], yilan_hizi, yilan_hizi))

    # Puanı gösterme
    font = pygame.font.SysFont("Arial", 20)
    puan_metni = font.render(f"Puan: {puan}", True, (255, 255, 255))
    ekran.blit(puan_metni, (10, 10))

    pygame.display.update()  # Ekranı güncelle
    clock.tick(15)  # FPS
