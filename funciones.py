def get_hydro_year(date_, start_month=7):

  '''
  Función que define el año hidrológico
  en el caso del proyecto este se define entre el -> 1/agosto al 31/julio
  '''

  year = date_.strftime('%Y')
  month = date_.strftime('%m')
  offset = 1 if int(month) >= start_month - 1 else 0
  hydro_year = int(year) + offset - 1
  return hydro_year
