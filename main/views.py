import qrcode
from django.shortcuts import render
import qrcode.image.svg
# Create your views here.
from io import BytesIO
import time
from django.conf import settings
from qrcode.image.pure import PyPNGImage

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

def Homepage(request):
    if request.method == 'POST':
        data = request.POST['qr']
        img = qrcode.main.make(data,box_size=2,version=7, border=50,image_factory=StyledPilImage)
        img_name = 'qr' + str(time.time()) + '.png'
        img.save(f'media/{img_name}.png')
        with open(f'media/{img_name}.png', 'rb') as img_name:
            return render(request, 'main/index.html', {'img_name': img_name})
    return render(request, 'main/index.html')