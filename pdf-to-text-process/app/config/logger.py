import logging

# Configura el logger
logger = logging.getLogger('converter-pdf-text')
logger.setLevel(logging.DEBUG)  # Configura el nivel de logging deseado

# Define el formato de los logs
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Crea un manejador de consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# Añade los manejadores al logger
logger.addHandler(console_handler)
