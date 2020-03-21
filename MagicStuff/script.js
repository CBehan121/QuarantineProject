
var list=new Array;
function pickCom()
{

	document.location.href = "./pickCom.html"

}
function goStart()
{	
	document.location.href = "./index.html"
	
}
function goMono()
{
	
	console.log("hello");
	var imageURL = list.pop();
	show_image(imageURL, 276,110, "Google Logo");
	console.log(imageURL);
}
function getCards()
{
	fetch('https://api.scryfall.com/cards/search?order=cmc&q=c%3Ared+pow%3D3')
		.then(res => res.json())
		.then(json => {
			let searchResults = json.data;
			var imageSearch = searchResults[24].image_uris;
			console.log(imageSearch)
			list.push(imageSearch);
		});
}

function show_image(src, width, height, alt) {
    var img = document.createElement("img");
    img.src = src;
    img.width = width;
    img.height = height;
    img.alt = alt;

    // This next line will just add it to the <body> tag
    document.body.appendChild(img);
}
