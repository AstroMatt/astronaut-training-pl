var body = document.getElementsByTagName('body')[0];

for (let entry of Bibliography) {
    let id = Bibliography.indexOf(entry) + 1;
    let name = new RegExp('\\['+entry.title+'\\]', 'g');
    let index = '['+id+']';
    body.innerHTML = body.innerHTML.replace(name, index);
}
