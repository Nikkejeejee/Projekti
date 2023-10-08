def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * (width + 2) + '┐']
    for s in lines:
        res.append('│ ' + (s + ' ' * width)[:width] + ' │')
    res.append('└' + '─' * (width + 2) + '┘')
    return '\n'.join(res)

sairas = "˚‧º·sairas‧º·˚"

intro_text = f" ZZUPP loser! Oletko valmis pelaamaan nostalgia ruokapeliä?\n" \
             "\n Olet sairas.\n" \
             f"\n Kyllä luit oikein. Olet sairas.\n" \
             "\n Sairastat tautia nimeltään muistimakutauti.\n" \
             f" Hyvä asia on kuitenkin se, että olet voittanut 15 lentolippua. \n" \
             " Haluat syödä nostalgista ruokaa ennen kuin sairaus syö sinut. \n" \
             " Matkustat siis ympäri maailmaa syödäksesi nämä ruuat."
print(bordered(intro_text))
