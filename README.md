## FSE - Experimento I2C/BME280

### Execução
#### Python
* Dentro da pasta `python` executar o comando `python3 i2c.py`

#### C
* Dentro da pasta `c`, compilar o projeto com `gcc i2c.c bme280.c -I . -o bin`
* Rodar o executável gerado, `./bin`
* O arquivo com as medições será criado na mesma pasta e é chamado `out`.