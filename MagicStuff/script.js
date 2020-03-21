function pickCom()
{

	document.location.href = "./pickCom.html";

}
function goStart()
{	
	document.location.href = "./index.html";
	
}

function goMono()
{
	var imageURL = list[0];
	document.getElementById("att").src = imageURL;
	renderImages(list); 
	event.preventDefault();
	
}


var list=new Array;
fetch('https://api.scryfall.com/cards/search?order=cmc&q=c%3Ared+pow%3D3')
	.then(res => res.json())
	.then(json => {
		let searchResults = json.data;
		var imageSearch = searchResults[24].image_uris;
		list.push(imageSearch.small);
		
		
	});

let images = [
		'https://preview.redd.it/jwhen2f4j1o41.jpg?width=960&crop=smart&auto=webp&s=1cf097583580af1b05625453974aa0c2e640eddd',
		'https://i.redd.it/uji1ekm8h1o41.jpg',
		'https://preview.redd.it/wf9l4pryq1o41.jpg?width=960&crop=smart&auto=webp&s=ae5203f49606b21d43f202fe2bde6f3060b97787'
		]
		
function renderImages(imgList) {
		let s = '<div id="root">'
		imgList.forEach((imgUrl) => {
			s = s + `<img src=${imgUrl} />`
		})
		s = s + '</div>'
		document.getElementById("root").innerHTML = s
		}
		
		



