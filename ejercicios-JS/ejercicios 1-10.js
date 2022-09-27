function contar_caracteres(leter){

    if(Array.isArray(leter)){
        array_aplanado = leter.flat(Infinity)
        count = 0;
        for (let i = 0; i < array_aplanado.length; i++) {
            count = count + array_aplanado[i].length;
            
        }
        console.log("Tiene ", count ,"letras")

    }
    else if(isNaN(leter) == false){
        console.log("Por favor seleciona una palabra")
    }
    else{
        console.log("Tiene ",leter.length,"letras")
    };
};

let algoSUMPREMO = ['A', 'L', 'G', 'O', 'Supremo', 'ALGO']

// ejercicio 2