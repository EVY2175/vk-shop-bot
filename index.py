import json
def handler(event, context):
    # Данные от ВКонтакте приходят в формате JSON
    body = json.loads(event.get('body', '{}'))
    
    # 1. Подтверждение сервера для ВК (обязательно!)
    # Вставь сюда строку, которую дает тебе ВК в разделе Callback API
    SECRET_CONFIRMATION_STRING = "ТВОЯ_СТРОКА_ИЗ_ВК"
    
    if body.get('type') == 'confirmation':
        return {
            'statusCode': 200,
            'body': SECRET_CONFIRMATION_STRING
        }
    
    # 2. Обработка входящих сообщений
    if body.get('type') == 'message_new':
        # Здесь будет логика ответов бота
        return {
            'statusCode': 200,
            'body': 'ok'
        }
        
    return {
        'statusCode': 200,
        'body': 'ok'
    }