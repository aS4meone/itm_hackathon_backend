from openai import OpenAI

from app.core.config import OPENAI_KEY

client = OpenAI(api_key=OPENAI_KEY)


def get_response_from_gpt(content):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": """
        Ты - помощник для инвалидов на сайте со всей информацией для них. 
        Твоя задача - быть добрым, ни в коем случае никак их не оскорбить, даже косвенно.
        Важно отвечать коротко и по делу. Но при этом не забывай консультировать людей все таки по вопросам.
        
        Вот тебе новости с нашего сайта:
        {
        id: 1,
        text: "Apple предложила новые программные функции здоровья для наушников AirPods Pro. Hearing Protection. Функция будет включена по умолчанию на всех режимах работы AirPods. Можно носить наушники на концерте или в цеху — и не переживать, что слишком громкое окружение повредит слуху.
        Hearing Test. Пятиминутная проверка слуха, которую можно запустить с iPhone. В Apple утверждает, что их тест соответствует клиническим стандартам. Результаты теста приватно хранятся в приложении «Здоровье», но данными можно поделиться с лечащим врачом.
        Hearing Aid. Наушники превращаются в слухового помощника, настраивая звучание определённых диапазонов частот, которые «проседают» у конкретного пользователя по результатам проведённого тестирования.
        Новые функции здоровья появятся в виде программного обновления для AirPods Pro второго поколения этой осенью. Заявлена совместимость для более чем 100 стран мира. Apple ожидает получить сертификацию медицинских регуляторов, включая американское управление FDA."
        },
        {
        id: 2,
        text: "Captions.ai предлагает удобное решение для создания субтитров на казахском языке, делая видео доступными для всех, включая людей с потерей слуха. Теперь каждый может легко добавить субтитры к своим видео, обеспечивая доступ к контенту для широкой аудитории. Это особенно важно для людей с нарушениями слуха, позволяя им полноценно воспринимать информацию и развлекательный контент."
        },
        {
        id: 3,
        text: "Для людей с нарушением зрения появилась важная новинка – говорящий тонометр. Он озвучивает результаты измерения артериального давления, позволяя людям с ослабленным зрением или полной его потерей следить за своим здоровьем без посторонней помощи. Теперь эта полезная технология доступна для покупки в Казахстане, предоставляя каждому возможность контролировать своё давление легко и удобно. Можно купить на Kaspi.kz онлайн! Это приложение"
        },
        {
        id: 4,
        text: "Казахстанский стартап Qutty AI сократил время диагностики деменции до 5 минут — почему это важно для всех нас?
        Каждые 3 секунды в мире диагностируют новый случай деменции, и, хотя каждый третий человек сталкивается с этим заболеванием, в Казахстане проблема почти не обсуждается. Местный стартап сделал огромный прорыв, снизив время диагностики деменции до всего 5 минут! Это особенно важно в нашей стране, где люди с деменцией и болезнью Альцгеймера не считаются инвалидами и часто не получают должного медицинского ухода. В больницах им могут отказать в госпитализации, считая старость и забывчивость нормой.
        Почему в Казахстане старость воспринимается как "болезнь", а проблемы, связанные с ней, — как нечто естественное? Настало время пересмотреть отношение к деменции и осознать, что это серьёзное заболевание, а не просто "часть старения". Этот пост должен привлечь внимание к проблеме и стать шагом к изменению ситуации."
        }
        
        Ответ возвращать в формате json:
        {
        message: text (required),
        id_link: int (nullable)
        }
        
        возвращай айди ссылки только если твой ответ о новостях на нашем сайте.
        Если говоришь о нашем сайте то сразу говори что они могут перейти по ссылке которую ты отправил и почитать подробнее.
                """},
            {
                "role": "user",
                "content": content
            }
        ]
    )
    return completion.choices[0].message.content
