from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def greeting_keyboard():
    keyboard = VkKeyboard(one_time=False, inline=True)
    keyboard.add_button(f'&#127757;', payload={"Command": "start"},
                        color=VkKeyboardColor.POSITIVE)
    keyboard = keyboard.get_keyboard()
    return keyboard
