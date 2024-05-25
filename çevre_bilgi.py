import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

# Ana menü komutu
@bot.command()
async def info_menu(ctx):
    menu = (
        "Çevreye önem veren ve çevre dostu uygulamalar ve atıkları azaltmanın yolları hakkında daha fazla bilgi edinmek isteyen kişiler için şunları yapabilirsiniz:\n\n"
        "**1. Çevresel İpuçları:** !ipucu\n"
        "**2. Geri Dönüşüm Bilgileri:** !geridönüşüm\n"
        "**3. Doğa Dostu Alışveriş Tavsiyeleri:** !alışveriş\n"
        "**4. Atık Azaltma Stratejileri:** !atıkazaltma\n"
        "**5. Çevre Dostu Etkinlikler:** !etkinlikler\n"
        "**6. Çevre Haberleri:** !haberler"
    )
    await ctx.send(menu)

# Aşağıda bu komutların içeriklerini doldurabilirsiniz:
@bot.command()
async def ipucu(ctx):
    tips = (
        "Çevresel İpuçları:\n\n"
        "1. Tek kullanımlık plastikleri kullanmaktan kaçının.\n"
        "2. Enerji tasarruflu ampuller kullanın.\n"
        "3. Su tüketiminizi azaltın, gereksiz yere muslukları açık bırakmayın.\n"
        "4. Bisiklet kullanın veya toplu taşıma araçlarını tercih edin.\n"
        "5. Kendi çantanızı kullanarak alışveriş yapın."
    )
    await ctx.send(tips)

# geri dönüşüm
@bot.command()
async def recycling_info(ctx):
    recycling = (
        "Geri Dönüşüm Bilgileri:\n\n"
        "1. Kağıt ve kartonları ayrı bir şekilde toplayın.\n"
        "2. Cam şişeleri ve kavanozları temizleyerek geri dönüştürün.\n"
        "3. Plastik şişeleri sıkıştırarak geri dönüşüm kutusuna atın.\n"
        "4. Metal kutuları ve alüminyum folyo gibi materyalleri geri dönüştürün.\n"
        "5. Elektronik atıkları uygun geri dönüşüm merkezlerine götürün."
    )
    await ctx.send(recycling)

# alışveriş
@bot.command()
async def alışveriş(ctx):
    alisveris = (
        "Doğa_Dostu_Alışveriş_Tavsiyeleri:\n\n"
        "1. Çocuklara oyunca alırken %100 doğal alın."
        "2."
        "3."
        "4."
        "5."
    )
    await ctx.send(alisveris)

# alışveriş
@bot.command()
async def atık_azaltma(ctx):
    atik = (
        "Atık Azaltma Stratejileri:\n\n"
        "1. Çocuklara oyunca alırken %100 doğal alın.\n"
        "2."
        "3."
        "4."
        "5."
    )
    await ctx.send(atik)

# alışveriş
@bot.command()
async def etkinlikler(ctx):
    etkinlik = (
        "Çevre Dostu Etkinlikler:\n\n"
        "1. En fazla ağacı dikme etklinliği\n"
        "2."
        "3."
        "4."
        "5."
    )
    await ctx.send(etkinlik)

# alışveriş
@bot.command()
async def haberler(ctx):
    haberler = (
        "Çevre Etkinlikleri:\n\n"
        "1. Çocuklara oyunca alırken %100 doğal alın.\n"
        "2."
        "3."
        "4."
        "5."
    )
    await ctx.send(haberler)





bot.run("")
