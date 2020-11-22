```bash
>>> from articles.models import Article,Comment
>>> from django.contrib.auth import get_user_model
>>> users = get_user_model()
>>> saladin = users.objects.get(username='saladin')
>>> z = Article(title='Software Spring',body='World is being eaten by softwares,but who is eating softwares? Machine Learning!',author = saladin)
>>> z.save()
>>> x = Comment(article = Article.objects.get(id=8),comment='well this is fast rising,indeed',author = get_user_model().objects.get(username='nuruddin'))
>>> x.save()
>>> or,
>>> x = Comment(article = z ,comment='well this is fast rising,indeed',author = get_user_model().objects.get(username='nuruddin'))
```
