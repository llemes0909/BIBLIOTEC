from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    def __str__(self):
        return f'{self.nome}, {self.uf}'

class Autores(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    def __str__(self):
         return f'{self.nome}, {self.site}, {self.cidade}'
    
class Genero(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    
class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome}, {self.site}, {self.cidade}'
    
class Leitor(models.Model):
    nome = models.CharField(max_length=100)
    email =  models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    def __str__(self):
        return f'{self.nome}, {self.email}, {self.cpf}'

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    preco = models.IntegerField()
    data_plub = models.DateField()
    status = models.BooleanField()
    def __str__(self):
        return f'{self.nome}, {self.autor}, {self.editora}, {self.genero}, {self.preco}, {self.data_plub}, {self.status}'

class Emprestimo(models.Model):
    data_empr = models.DateField()
    data_devolucao = models.DateField()
    leitor= models.ForeignKey(Leitor, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.data_empr}, {self.data_devolucao}, {self.leitor}, {self.livro}'

    


