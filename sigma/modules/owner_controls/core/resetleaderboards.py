# Apex Sigma: The Database Giant Discord Bot.
# Copyright (C) 2017  Lucia's Cipher
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import discord

from sigma.core.mechanics.command import SigmaCommand


async def resetleaderboards(cmd: SigmaCommand, message: discord.Message, args: list):
    await cmd.db[cmd.db.db_cfg.database].Cookies.update_many({}, {"$set": {"Cookies": 0}})
    await cmd.db[cmd.db.db_cfg.database].CurrencySystem.update_many({}, {"$set": {"global": 0}})
    await cmd.db[cmd.db.db_cfg.database].ExperienceSystem.update_many({}, {"$set": {"global": 0}})
    response = discord.Embed(color=0xFFCC4D, title=f'🔥 The global leaderboards have been destroyed.')
    await message.channel.send(embed=response)

