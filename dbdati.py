import datetime


def sodien(c):
  sodien = datetime.date.today()
  # rit = datetime.date.today() + datetime.timedelta(days=1)
  # sodien.month
  # sodien.day
  # sodien.year

  c.execute('SELECT vards FROM vardadienas WHERE menesis=? AND diena=?', (sodien.month, sodien.day))
  vardi = c.fetchall()
  return vardi


def menesa_vardi(c, menesis):
  c.execute('SELECT vards FROM vardadienas WHERE menesis=?', (menesis,))
  vardi = c.fetchall()
  return vardi


def varda_datums(c, vards):
  c.execute('SELECT menesis, diena FROM vardadienas WHERE vards=?', (vards,))
  datums = c.fetchone()
  return datums


def mekle_pec_burtiem(c, burti):
  c.execute('SELECT vards FROM vardadienas WHERE vards LIKE ?', ('%'+burti+'%', ))
  vardi = c.fetchall()
  return vardi


def mekle_pec_burtiem2(c, s, b):
  c.execute('SELECT vards FROM vardadienas WHERE vards LIKE ?', (s+'%'+b, ))
  vardi = c.fetchall()
  return vardi


def statistika(c, menesis='visi'):
  if menesis == 'visi':
    c.execute('''SELECT menesis, diena, count(vards) from vardadienas GROUP BY menesis, diena ORDER BY menesis ASC, diena ASC''')
  else:
    c.execute('SELECT menesis, diena, count(vards) from vardadienas WHERE menesis=? GROUP BY menesis, diena ORDER BY menesis ASC, diena ASC', (menesis,))
  return c.fetchall()
