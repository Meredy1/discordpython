import discord
from discord.ext import commands
import random
from webserver import keep_alive
import os



intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="!",
                      case_insensitive=True,
                      intents=intents)


@client.event
async def on_ready():
    print('Entramos como {0.user}'.format(client))


@client.command()
async def ola(ctx):
    await ctx.send(f'Ola,{ctx.author}')

@client.command()
async def ping(ctx):
    await ctx.send('pong')


@client.command()
async def historia(ctx):
    embed = discord.Embed(
        title=
        'Organização Criada em Abril de 2019 com intuito de trazer sempre os melhores campeonatos.',
        description=
        'Torneio organizado pela equipe amadora de League of Legends, NSW-Never Stop Winning. A NSW-Never Stop Winning traz a oportunidade para players dos mais diversos elos mostrarem suas habilidades em equipe  e assim evoluir suas mecânicas em game, ou até mesmo avançar em uma carreira profissional de League of Legends.',
        colour=11598249)

    embed.set_author(
        name='┃Historia da NsW',
        icon_url=
        'https://firebasestorage.googleapis.com/v0/b/battlefy-2f59d.appspot.com/o/user-imgs%2F5a6fae674475f803844ad8e9%2F1562118063661.png?alt=media&token=cb708ea8-01b5-416e-a747-9058d7325003'
    )

    embed.set_thumbnail(url='https://i.imgur.com/0i1W5cB.gif')

    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/580468808117125131/710129327387443250/historia.png'
    )

    embed.set_footer(text='Never Stop Winning 2019-2021 ®')

    embed.add_field(name='Para mais informações acesse:',
                    value='https://battlefy.com/never-stop-winning',
                    inline=False)
    embed.add_field(name='Nosso Twitter:',
                    value='https://twitter.com/NSW_Oficial',
                    inline=True)
    embed.add_field(name='Nossa Pagina no Facebook:',
                    value='https://www.facebook.com/GoNsw/',
                    inline=True)

    await ctx.send(embed=embed)


@client.event
async def on_member_join(member):
    canalboasvindas = client.get_channel(584454331550662669)
    regras = client.get_channel(797543242350460998)
    registro = client.get_channel(797544359373307987)
    mensagem = await canalboasvindas.send(
        f"<:NSW:576855687892697109> Bem-vindo {member.mention}, sinta-se à vontade para conversar chat do Laboratório!                                                                                                                        ⤷ Leia as regras em {regras.mention};                                                                            ⤷ Faça seu registro em {registro.mention}."
    )


@client.command()
async def premio(ctx):
    embed = discord.Embed(
        description='Em caso de duvidas,contactar um dos administradores.',
        colour=11598249)

    embed.set_author(
        name='┃Premiação',
        icon_url='https://elojobhigh.com.br/assets/img/icone-riot-points.png')

    embed.set_thumbnail(
        url='https://media1.giphy.com/media/THmnFbwUxk2J8l734K/giphy.gif')

    embed.set_image(url='')

    embed.set_footer(text='Never Stop Winning 2019-2021 ®')

    embed.add_field(name='1° Lugar: 2000 RP + Ryze Triunfante',
                    value='2° Lugar: 1600 RP',
                    inline=False)
    embed.add_field(name='3° Lugar: 800 RP',
                    value='4° Lugar: Bônus de XP (25 Vitórias)',
                    inline=True)
    embed.add_field(name='Para mais informações acesse:',
                    value='https://battlefy.com/never-stop-winning',
                    inline=True)

    await ctx.send(embed=embed)

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
