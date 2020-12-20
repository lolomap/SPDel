import vk_manage
import msvcrt
import os

while True:
    print('Вбей через пробел два числа: первое это первая фотка, вторая - вторая\n'
          'всё включительно.\n')
    x1 = int(input())
    x2 = int(input())
    vk_manage.photo_del(vk_manage.choose_photos(x1, x2))
    print('Я удалил это дерьмо, ёпта. Жмякни чтонить чтоб удалить еще чтото\n'
          'или вырубай прогу с коронной двоечки\n')
    msvcrt.getch()
    os.system('cls')
