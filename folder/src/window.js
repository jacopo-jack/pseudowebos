    // metodo window.screen  e gestore sfondo
    if (window.screen) { 
		var w = screen.availWidth; 
		var h = screen.availHeight;
		window.moveTo(0, 0); 
		window.resizeTo(w, h); 
	} 
    // funzioni window.open
    function hub(){
        var h = screen.height;
	if(w >= "1280"){
		larghezza = 1050;
		altezza = 450;
	}else{
		larghezza = 700;
		altezza = 300;
	}
	var x = Math.round(w / 2) - Math.round(larghezza / 2);
	var y = Math.round(h / 2) - Math.round(altezza / 2);
	var finestra = window.open(
        'https://jacopo-jack.github.io/webhub/', 
        null, 
        'left=' + x + ',screenX=' + x + ',top=' + y + ',screenY=' + y + ',width=' + larghezza + ',height=' + altezza
    );

    // dopo torna alla home
    window.location.href = "index.html"; // Assegnazione corretta
    }
    function console(){
        var h = screen.height;
	if(w >= "1280"){
		larghezza = 1050;
		altezza = 450;
	}else{
		larghezza = 700;
		altezza = 300;
	}
	var x = Math.round(w / 2) - Math.round(larghezza / 2);
	var y = Math.round(h / 2) - Math.round(altezza / 2);
	var finestra = window.open(
        'console.html', 
        null, 
        'left=' + x + ',screenX=' + x + ',top=' + y + ',screenY=' + y + ',width=' + larghezza + ',height=' + altezza
    );

    // dopo torna alla home
    window.location.href = "index.html"; // Assegnazione corretta
    }



    function workbench(){
        var h = screen.height;
	if(w >= "1280"){
		larghezza = 1050;
		altezza = 450;
	}else{
		larghezza = 700;
		altezza = 300;
	}
	var x = Math.round(w / 2) - Math.round(larghezza / 2);
	var y = Math.round(h / 2) - Math.round(altezza / 2);
	var finestra = window.open(
        'workbench.html', 
        null, 
        'left=' + x + ',screenX=' + x + ',top=' + y + ',screenY=' + y + ',width=' + larghezza + ',height=' + altezza
    );

    // dopo torna alla home
    window.location.href = "index.html"; // Assegnazione corretta
    }
	function store(){
        var h = screen.height;
	if(w >= "1280"){
		larghezza = 1050;
		altezza = 450;
	}else{
		larghezza = 700;
		altezza = 300;
	}
	var x = Math.round(w / 2) - Math.round(larghezza / 2);
	var y = Math.round(h / 2) - Math.round(altezza / 2);
	var finestra = window.open(
        'store.html', 
        null, 
        'left=' + x + ',screenX=' + x + ',top=' + y + ',screenY=' + y + ',width=' + larghezza + ',height=' + altezza
    );

    // dopo torna alla home
    window.location.href = "index.html"; // Assegnazione corretta
    }