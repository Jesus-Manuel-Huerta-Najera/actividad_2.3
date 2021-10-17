import web
import sklearn
from joblib import load

urls = (
    '/', 'Index',
)
app = web.application(urls, globals())
render = web.template.render("view")

class Index:

    model = load("model.joblib")

    def GET(self):
        result = None
        return render.index(result)
    def POST(self):
        form = web.input()
        x = float( form.x)
        xs=[]
        xs.append([x])
        result = self.model.predict(xs)
        print(x)
        return render.index(result)
if __name__ == "__main__":
    app.run()