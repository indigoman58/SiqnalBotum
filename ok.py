
import asyncio
import random
from datetime import datetime, timedelta
from telegram import Bot

# Telegram botunuzun tokeni və kanal ID'sini buraya yazın
TOKEN = '7852481303:AAH-4lDQno4GGS-xFbj-c8cvDckOIuk9luI'
CHANNEL_ID = '-1002096914925'  # Kanal ID'sini eksi işarəsi ilə başlatmayı unutmayın

bot = Bot(token=TOKEN)

# Gözəl adlar və soyadlar
male_first_names = [
    'Əli', 'Vəli', 'Səid', 'Hüseyn', 'Elxan', 'Rauf', 'Elmir', 'Ramin', 'Fərid', 'Nail', 'Rəşad', 'Tural',
    'Orxan', 'Rövşən', 'Kamran', 'Aydın', 'Bəşarət', 'Kənan', 'Sami', 'Mübariz', 'Natiq', 'Yusif', 'Vüqar',
    'Vüsal', 'Ramil', 'Kamil', 'Fikrət', 'Vahid', 'Eldar', 'Fərhad', 'Rəşid', 'Sadiq', 'Aqil', 'Zaur',
    'Mikayıl', 'Anar', 'Nəriman', 'Cavid', 'Pərviz', 'Müslüm', 'Şahin', 'Hikmət', 'Zeynal', 'Cəlal', 'Samir',
    'Səbuhi', 'Əmrah', 'Təbriz', 'Rəhim', 'Təhməz', 'Araz', 'Kamal', 'Nəcib', 'Güloğlu', 'Rauf', 'Müslüm'
]

female_first_names = [
    'Nigar', 'Leyla', 'Rəna', 'Mətanət', 'Günay', 'Xanım', 'Seda', 'Nərmin', 'Aysel', 'Lalə', 'Fidan',
    'Gülnar', 'Tülin', 'Zeynəb', 'Zəhrə', 'Şəbnəm', 'Səmayə', 'Rüxsarə', 'Şəhla', 'Sona', 'Nəzakət',
    'Ləman', 'Fərqanə', 'Dilarə', 'Aygün', 'Sahiba', 'Rüya', 'Təranə', 'Günəş', 'Səbinə', 'Gülər', 'Sənubər',
    'Yasəmən', 'Cavidan', 'Mələk', 'Sevinc', 'Bahar', 'Nigar', 'Nərgiz', 'Qəmər', 'Səma', 'Sona', 'Rüya',
    'Günel', 'Xəyalə', 'Mələk', 'Əsmər', 'Ləman', 'Səbinə', 'Fəridə', 'Gülnar', 'Vüsalə', 'Zülfiyyə', 'İnci'
]

male_last_names = [
    'Hüseynov', 'Əliyev', 'Məmmədov', 'Quliyev', 'Rəhimov', 'Həsənov', 'Ağayev', 'Şıxlı', 'Məhərrəmov', 'Səfərov',
    'Qasımov', 'Babayev', 'Rüstəmov', 'Zeynallı', 'Novruzov', 'Əsgərov', 'Hacızadə', 'Yusifov',
    'Gözəlov', 'Bünyatov', 'Məlikov', 'Çingizov', 'Sadiqov', 'Elçinov', 'Şirinov', 'Ələsgərov', 'Fərhadov',
    'Nəbiyev', 'Vəliyev', 'Rəsulov', 'İsmayılov', 'Muradov', 'Eldarov', 'Yusifov', 'Xəlilov', 'Sadiqov',
    'Babayev', 'Əhmədov', 'Kərimov', 'Fərhadov', 'Təhməzov', 'Həsənov', 'Novruzov'
]

female_last_names = [
    'Hüseynova', 'Əliyeva', 'Məmmədova', 'Quliyeva', 'Rəhimova', 'Həsənova', 'Ağayeva', 'Şıxlı', 'Məhərrəmova',
    'Səfərova', 'Qasımova', 'Babayev', 'Rüstəmova', 'Zeynallı', 'Novruzova', 'Əsgərova', 'Hacızadə', 'Yusifova',
    'Gözəlova', 'Bünyatova', 'Məlikova', 'Ağayeva', 'Hacızadə', 'Çingizova', 'Sadiqova', 'Elçinova', 'Şirinova',
    'İsmayılova', 'Fəridə', 'Rüxsarə', 'Nigarova', 'Rəşidova', 'Şəhla', 'Nigar', 'Günay', 'Xanım', 'Mələk',
    'Leyla', 'Zeynəb', 'Aysel', 'Tülin', 'Günel', 'Aygün', 'Sahiba', 'Fərqanə', 'Günel', 'Şəbnəm'
]

def generate_random_user_earnings(num_users=25):
    earnings = []
    for _ in range(num_users):
        if random.choice([True, False]):
            first_name = random.choice(male_first_names)
            last_name = random.choice(male_last_names)
        else:
            first_name = random.choice(female_first_names)
            last_name = random.choice(female_last_names)
        
        name = "{} {} 🌟✨🎉".format(first_name, last_name)
        earnings.append((name, random.randint(20, 100)))
    
    return earnings

async def send_earnings_message():
    users_earnings = generate_random_user_earnings()
    earnings_message = (
        "🎉✨ SON 1 SAATİN QAZANCI 🎉✨\n\n"
        "⭐️ 25 nəfərin son 1 saat ərzində qazancı:\n"
        "{}\n\n"
        "💵 Mütləq sizlərdə Qeydiyyatdan keçin və qazanmağa başlayın! 🔥\n\n"
        "🚀 Bizim bot-un verdiyi siqnallarla çoxunun həyatı dəyişdi! 🌟"
    ).format('\n'.join('{} {} manat qazandı 💰'.format(name, earnings) for name, earnings in users_earnings))
    
    try:
        await bot.send_message(chat_id=CHANNEL_ID, text=earnings_message, parse_mode='Markdown')
        print("Qazanc mesajı göndərildi! ✅")
    except Exception as e:
        print(f"Qazanc mesajı göndərilərkən xəta baş verdi: {e}")

async def send_bet_message(random_time):
    message = (
        f"🎯 Bu günün mərci 🎯\n\n"
        f"⏰ Saat {random_time}-də mərc edin! 💸\n\n"
        f"🎮 Aviator oyunu 🎮\n\n"
        f"📉 2x də mərci dayandırın.\n\n"
        f"🌟 Mütləq sizlərdə Qeydiyyatdan keçin və qazanmağa başlayın! 🚀\n\n"
        f"Uğurlar! 🍀"
    )
    try:
        await bot.send_message(chat_id=CHANNEL_ID, text=message, parse_mode='Markdown')
        print("Mərclə bağlı mesaj göndərildi! ✅")
    except Exception as e:
        print(f"Mesaj göndərilərkən xəta baş verdi: {e}")

async def automate_bet():
    while True:
        random_time = get_random_future_minute()
        await send_bet_message(random_time)
        await asyncio.sleep(8 * 60)  # 8 dəqiqə gözləyir

def get_random_future_minute():
    now = datetime.now()
    future_minute = (now + timedelta(minutes=random.randint(2, 6))).strftime("%H:%M")
    return future_minute

async def automate_messages():
    while True:
        await send_earnings_message()
        await asyncio.sleep(60 * 60)  # 1 saat gözləyir

async def main():
    # İki funksiyanı eyni vaxtda işlətmək üçün
    await asyncio.gather(
        automate_messages(),  # Qazanc mesajlarını 1 saat aralığı ilə göndərir
        automate_bet()  # Mərc mesajlarını 8 dəqiqə aralığı ilə göndərir
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Proqram dayandırıldı.")
