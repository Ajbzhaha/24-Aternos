from nextcord.ui import button, View
from nextcord import Embed, ButtonStyle
import nextcord
from nextcord.ext import commands
import requests

# ------------- CONFIG MAIN-------------- #

token = ""
COLOR = 0xf8f8f8
PREFIX = "."
Images = "https://cdn.discordapp.com/attachments/1199386824582373516/1217869173737263164/kawaii.gif?ex=6605980d&is=65f3230d&hm=64a3c23c0b3728eeea6fc3d64b17077a641c34534d61d1ae8f9d87391fb5e609&"

# ------------- CONFIG EMOJI-------------- #

emoji_1 = "<a:DancingBlackCat:1198633069742141623>"
emoji_2 = "<a:Black_CatLinguinha:1198632831488897107>"
emoji_3 = "<a:BlackCat:1198631834087592011>"
emoji_4 = "<a:Cat:1198632579834851350>"
emoji_5 = "<:dawdas:1202987022994776145>"
emoji_6 = "<a:9668milkpink:1210538683862618152>"
emoji_7 = "<a:i6:1210538767329267712>"
emoji_8 = "<a:891080282394988544:1210538719027929150>"
emoji_9 = "<a:891080297062465546:1210538720881676318>"
emoji_10 = "<a:DG:1179111269039624223>"
emoji_11 = "<a:emoji_9:1160527285422669834>"
emoji_12 = "<a:DG12:1092803516919205888>"

# ------------- CONFIG EMOJI-------------- #

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, help_command=None, intents=intents)


class NSFW(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Vtuber NSFW", style=ButtonStyle.primary, emoji=emoji_1)
    async def send_vtuber(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "vtuber")

    @button(label="Pussy NSFW", style=ButtonStyle.primary, emoji=emoji_2)
    async def send_anime(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "pussy")

    @button(label="Creampie NSFW", style=ButtonStyle.primary, emoji=emoji_3)
    async def send_wallpaper(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "creampie")

    @button(label="Neko NSFW", style=ButtonStyle.primary, emoji=emoji_4)
    async def send_neko_nsfw(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "nsfw-neko")

    @button(label="Random NSFW", style=ButtonStyle.primary, emoji=emoji_5)
    async def send_cosplay(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "random")

    @button(label="Ass NSFW", style=ButtonStyle.primary, emoji=emoji_6)
    async def send_ass(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "ass")

    @button(label="Ecchi NSFW", style=ButtonStyle.primary, emoji=emoji_7)
    async def send_ecchi(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "ecchi")

    @button(label="Ai NSFW", style=ButtonStyle.primary, emoji=emoji_8)
    async def send_ai_nsfw(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "ai")

    @button(label="Boobs NSFW", style=ButtonStyle.primary, emoji=emoji_9)
    async def send_boobs(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "boobs")

    @button(label="Paizuri NSFW", style=ButtonStyle.primary, emoji=emoji_10)
    async def send_aizuri(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "paizuri")

    @button(label="Neko", style=ButtonStyle.primary, emoji=emoji_12)
    async def send_neko(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "neko")

    @nextcord.ui.button(
        label='Waifu Api NSFW',
        emoji="<a:i7:1210538764905087046>",
        style= nextcord.ButtonStyle.blurple
    )
    async def send(self, button: nextcord.Button, interaction: nextcord.Interaction):
        msg = await interaction.response.send_message('Please wait...', ephemeral=True)
        api = 'https://api.waifu.pics/nsfw/waifu'

        try:
            response = requests.get(api)
            if response.status_code == 200:
                url = response.json()['url']

                embed = Embed(
                    title=f"**__WAIFU API__**\n",
                    description=f"Send by {interaction.guild.me.name}",
                    color=COLOR
                )
                embed.add_field(name="Api by", value="[Waifu](https://api.waifu.pics/nsfw/waifu)")
                embed.set_image(url)
                embed.set_footer(text="NSFW System", icon_url=interaction.guild.me.display_avatar.url)

                await interaction.user.send(embed=embed)

                await msg.edit(content='Send check Dms')
            else:
                await msg.edit(content='Sorry, the NSFW API is currently down. Please try again later.')
        except requests.RequestException as e:
            await msg.edit(content='Sorry, an error occurred while processing your request. Please try again later.')

    async def send_nsfw(self, interaction: nextcord.Interaction, category: str):
        msg = await interaction.response.send_message('Please wait...', ephemeral=True)
        api = f'https://nekos.pro/api/{category}/'

        try:
            response = requests.get(api)
            if response.status_code == 200:
                url = response.json()['url']

                embed = Embed(
                    title=f"**__{category.upper()}__**\n",
                    description=f"Send by {interaction.guild.me.name}",
                    color=COLOR
                )
                embed.add_field(name="Api by", value="[Neko Pro](https://nekos.pro/api/)")
                embed.set_image(url)
                embed.set_footer(text="NSFW System", icon_url=interaction.guild.me.display_avatar.url)

                await interaction.user.send(embed=embed)

                await msg.edit(content='Send check Dms')
            else:
                await msg.edit(content='Sorry, the NSFW API is currently down. Please try again later.')
        except requests.RequestException as e:
            await msg.edit(content='Sorry, an error occurred while processing your request. Please try again later.')

@bot.slash_command(
    name="nsfw_menu",
    description="Setup NSFW system"
)
async def nsfw_setup(interaction: nextcord.Interaction):
    if not interaction.user.guild_permissions.administrator:
        return await interaction.response.send_message(content='[ERROR] No Permission For Use This Command.', ephemeral=True)
    
    embed = nextcord.Embed(
        title="__NSFW System__",
        description="```คลิกปุ่มเพื่อสุ่มรูปอนิเมะ 18+\nรูปภาพจะทำการส่งไปไหน DMs นะ```",
        color=COLOR
    )
    embed.set_image(url=Images)
    embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon.url) 
    
    await interaction.channel.send(embed=embed, view=NSFW())
    await interaction.response.send_message(content='[SUCCESS] Done.', ephemeral=True)

@bot.event
async def on_ready():
    print(f"Started {bot.user.name}")

bot.run(token)