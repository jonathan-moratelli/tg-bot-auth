import telebot


API_KEY = '1457304861:AAF3LmYJ6GxgpK-8hTQP8o2caQNIyOONuKY'

bot = telebot.TeleBot(API_KEY, parse_mode='HTML')


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    print(mensagem)
    #bot.reply_to(mensagem, "<b>Olá aqui é o bot da XXXXX</b>")
    bot.send_message(mensagem.chat.id, "<b>Olá aqui é o bot da XXXXX</b>")


bot.polling()


mensagem = {'content_type': 'text',
            'id': 11,
            'message_id': 11,
            'from_user': {'id': 1376705790, 'is_bot': False, 'first_name': 'Jonathan', 'username': None, 'last_name': None, 'language_code': 'pt-br', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None, 'is_premium': None, 'added_to_attachment_menu': None}, 'date': 1675384026, 'chat': {'id': 1376705790, 'type': 'private', 'title': None, 'username': None, 'first_name': 'Jonathan', 'last_name': None, 'is_forum': None, 'photo': None, 'bio': None, 'join_to_send_messages': None, 'join_by_request': None, 'has_private_forwards': None, 'has_restricted_voice_and_video_messages': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None, 'slow_mode_delay': None, 'message_auto_delete_time': None, 'has_protected_content': None, 'sticker_set_name': None, 'can_set_sticker_set': None, 'linked_chat_id': None, 'location': None, 'active_usernames': None, 'emoji_status_custom_emoji_id': None, 'has_hidden_members': None, 'has_aggressive_anti_spam_enabled': None}, 'sender_chat': None, 'forward_from': None, 'forward_from_chat': None, 'forward_from_message_id': None, 'forward_signature': None, 'forward_sender_name': None, 'forward_date': None, 'is_automatic_forward': None, 'reply_to_message': None, 'via_bot': None,
            'edit_date': None, 'has_protected_content': None, 'media_group_id': None, 'author_signature': None, 'text': 'Teste', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'reply_markup': None, 'message_thread_id': None, 'is_topic_message': None, 'forum_topic_created': None, 'forum_topic_closed': None, 'forum_topic_reopened': None, 'has_media_spoiler': None, 'forum_topic_edited': None, 'general_forum_topic_hidden': None, 'general_forum_topic_unhidden': None, 'write_access_allowed': None, 'json': {'message_id': 11, 'from': {'id': 1376705790, 'is_bot': False, 'first_name': 'Jonathan', 'language_code': 'pt-br'}, 'chat': {'id': 1376705790, 'first_name': 'Jonathan', 'type': 'private'}, 'date': 1675384026, 'text': 'Teste'}}
