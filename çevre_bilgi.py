import discord
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
        "**2. Geri Dönüşüm Bilgileri:** !geridonusum\n"
        "**3. Doğa Dostu Alışveriş Tavsiyeleri:** !alisveris\n"
        "**4. Atık Azaltma Stratejileri:** !atikazaltma\n"
        "**5. Çevre Dostu Etkinlikler:** !etkinlikler\n"
        "**6. Çevre Haberleri:** !haberler"
    )
    await ctx.send(menu)

# Çevresel İpuçları
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

# Geri Dönüşüm Bilgileri
@bot.command(name="geridonusum")
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

# Doğa Dostu Alışveriş Tavsiyeleri
@bot.command(name="alisveris")
async def alisveris(ctx):
    alisveris = (
        "Doğa Dostu Alışveriş Tavsiyeleri:\n\n"
        "1. Yerel ve organik ürünler satın alın.\n"
        "2. Geri dönüştürülebilir veya biyolojik olarak parçalanabilir ambalajları tercih edin.\n"
        "3. Daha az ambalajlı ürünler seçin.\n"
        "4. İkinci el ürünler satın alın veya takas yapın.\n"
        "5. Plastik poşetler yerine bez çantalar kullanın."
    )
    await ctx.send(alisveris)

# Atık Azaltma Stratejileri
@bot.command(name="atikazaltma")
async def atik_azaltma(ctx):
    atik = (
        "Atık Azaltma Stratejileri:\n\n"
        "1. Yeniden kullanılabilir su şişeleri ve kahve bardakları kullanın.\n"
        "2. Gıda atıklarını kompost yapın.\n"
        "3. Gereksiz posta ve reklamları durdurun.\n"
        "4. Tek kullanımlık ürünlerden kaçının.\n"
        "5. Tamir edilebilecek eşyaları atmayın, tamir edin."
    )
    await ctx.send(atik)

# Çevre Dostu Etkinlikler
@bot.command(name="etkinlikler")
async def etkinlikler(ctx):
    etkinlik = (
        "Çevre Dostu Etkinlikler:\n\n"
        "1. Ağaç dikme etkinliklerine katılın.\n"
        "2. Çevre temizleme kampanyalarına gönüllü olun.\n"
        "3. Yerel çiftliklerde gönüllü çalışın.\n"
        "4. Çevre bilinci arttırma seminerlerine katılın.\n"
        "5. Doğa yürüyüşleri düzenleyin ve katılın."
    )
    await ctx.send(etkinlik)

# Çevre Haberleri
@bot.command(name="haberler")
async def haberler(ctx):
    haberler = (
        "Çevre Haberleri:\n\n"
        "1. Yerel ve küresel çevre ile ilgili haberleri takip edin.\n"
        "2. Çevre dostu yenilikler ve teknolojiler hakkında bilgi edinin.\n"
        "3. İklim değişikliği ile ilgili gelişmeleri izleyin.\n"
        "4. Doğal yaşamı koruma çabalarına dair haberleri takip edin.\n"
        "5. Çevre politikaları ve yasalarındaki değişiklikleri öğrenin."
    )
    await ctx.send(haberler)

bot.run("")
