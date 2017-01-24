var body = document.getElementsByTagName('body')[0];

for (let entry of Bibliography.references) {
    let id = new RegExp('\\[\@'+entry.id+'\\]', 'g');
    let number = Bibliography.references.indexOf(entry) + 1;
    let index = '['+number+']';
    console.log(id, index);
    body.innerHTML = body.innerHTML.replace(id, index);
}
