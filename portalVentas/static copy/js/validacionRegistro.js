if(window.location.pathname.includes('registro')){
    const $formulario = document.getElementById('registro-formulario');
    const $inputs = document.querySelectorAll('.input');
    const $checkBox = document.getElementById('registro-pasaporte');
    const $selects = document.querySelectorAll('.contenedor-selects__select');
    const $errores = document.querySelectorAll('.contenedor-inputs-error');
    
    const validarRut = rut => {
        let runReverse = rut.substr(0, rut.indexOf('-')).split('').reverse();
        dvUsuario = rut.substr(rut.indexOf('-') + 1, 1)
        multiplicar = [2, 3, 4, 5, 6, 7, 2, 3];
        resultadoUno = 0;
    
        for (let i = 0; i < runReverse.length; i++) {
            resultadoUno += runReverse[i] * multiplicar[i]
        }
    
        let resultadoDos = Math.trunc(resultadoUno / 11)
        resultadoTres = resultadoDos * 11
        resta = resultadoUno - resultadoTres
        dvCorrecto = 11 - resta
    
        switch (dvCorrecto) {
            case 10:
                dvCorrecto = 'K'
                break;
            
            case 11:
                dvCorrecto = 0
                break;
        }
    
        if (typeof dvUsuario === 'string' && typeof dvCorrecto === 'string') {
            return (dvUsuario.toUpperCase() === dvCorrecto) ? true : false;
        }else{
            return (parseInt(dvUsuario, 10) === parseInt(dvCorrecto, 10)) ? true : false;
        }
    }
    
    const inputLleno = {
        rut: false,
        fecha: false,
        nombre: false,
        paterno: false,
        materno: false,
        correo: false,
        celular: false,
        region : false,
        provincia : false,
        comuna : false,
        contrasenia1: false,
        contrasenia1: false
    };
    const expresiones = {
        contrasenia: /^\w{6,12}$/,
        direccion: /^[A-z0-9#,\s]{1,50}$/,
        email: /^[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+(?:[a-zA-Z]{2}|aero|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi|museum|name|net|org|pro|tel|travel)$/,
        fecha: /^[0-3][0-9]\/[0-1][0-9]\/\d{4}$/,
        numero: /^[0-9]{8,9}$/,
        run: /^\d{1,2}\.?\d{3}\.?\d{3}[-][0-9kK]{1}$/,
        texto: /^[a-zA-Z\s]+$/
    };
    
    const validarCampo = (input, expresion) => {
    
        let $inputName = input.target.name.substr(input.target.name.indexOf('_') + 1, input.target.name.length);
        // Valida que el input no sea el que contiene el rut
        if (input.target.name !== 'REGISTRO_RUT' && input.target.name !== 'REGISTRO_CONTRASENIA2') {
            // Evalua la expresion regular de acuerdo al valor del input
            if (expresion.test(input.target.value)) {
                // Se remueve el error cuando la expresion regular devuelve true
                document.querySelector(`div[name='REGISTRO_ERROR_${$inputName}']`).classList.remove('block');
                // Agrega un borde verde
                document.querySelector(`input[name='REGISTRO_${$inputName}']`).classList.add('border-green-500', 'focus:border-green-500', 'border-2');
                inputLleno[$inputName.toLowerCase().toLowerCase()] = true;
            } else {
                // En caso de que la expresion retorne false, se muestra el error
                document.querySelector(`div[name='REGISTRO_ERROR_${$inputName}']`).classList.add('block');
                // Se remueve las clases verdes
                document.querySelector(`input[name='REGISTRO_${$inputName}']`).classList.remove('border-green-500', 'focus:border-green-500', 'border-2');
                // Se agrega un color rojo al input
                document.querySelector(`input[name='REGISTRO_${$inputName}']`).classList.add('border-red-500', 'focus:border-red-500', 'border-2');
                inputLleno[$inputName.toLowerCase()] = false;
            }
    
            // Valida que el input sea el que contiene el rut
        } else if (input.target.name === 'REGISTRO_RUT') {
            // Evalua la expresion regular de acuerdo al valor del input
            // console.info(expresiones.run.test(input.target.value))
            if (expresiones.run.test(input.target.value)) {
                if ($checkBox.checked) {
                    inputLleno[$inputName.toLowerCase()] = true;
                } else {
                    (validarRut(input.target.value)) ? inputLleno[$inputName.toLowerCase()] = true: inputLleno[$inputName.toLowerCase()] = false;
                }
    
                if (inputLleno[$inputName.toLowerCase()] === true) {
                    // Se remueve el error cuando la expresion regular devuelve true
                    document.querySelector(`div[name='REGISTRO_ERROR_${$inputName}']`).classList.remove('block');
                    // Agrega un borde verde
                    document.querySelector(`input[name='REGISTRO_${$inputName}']`).classList.add('border-green-500', 'focus:border-green-500', 'border-2');
                } else {
                    document.querySelector(`div[name='REGISTRO_ERROR_${$inputName}']`).classList.add('block');
                    // Se remueve las clases verdes
                    document.querySelector(`input[name='REGISTRO_${$inputName}']`).classList.remove('border-green-500', 'focus:border-green-500', 'border-2');
                    // Se agrega un color rojo al input
                    document.querySelector(`input[name='REGISTRO_${$inputName}']`).classList.add('border-red-500', 'focus:border-red-500', 'border-2');
                }
            } else {
                document.querySelector(`div[name='REGISTRO_ERROR_${$inputName}']`).classList.add('block');
                // Se remueve las clases verdes
                document.querySelector(`input[name='REGISTRO_${$inputName}']`).classList.remove('border-green-500', 'focus:border-green-500', 'border-2');
                // Se agrega un color rojo al input
                document.querySelector(`input[name='REGISTRO_${$inputName}']`).classList.add('border-red-500', 'focus:border-red-500', 'border-2');
            }
    
            // Valida que el input sea el que contiene el la contrasenia2
        } else if (input.target.name === 'REGISTRO_CONTRASENIA2') {
            if (input.target.value === $inputs[8].value) {
                // Evalua la expresion regular de acuerdo al valor del input
                document.querySelector(`div[name='REGISTRO_ERROR_${$inputName}']`).classList.remove('block');
                document.querySelector(`input[name='REGISTRO_${$inputName}']`).classList.add('border-green-500', 'focus:border-green-500', 'border-2');
                inputLleno[$inputName.toLowerCase()] = true;
            } else {
                document.querySelector(`div[name='REGISTRO_ERROR_${$inputName}']`).classList.add('block');
                // Se remueve las clases verdes
                document.querySelector(`input[name='REGISTRO_${$inputName}']`).classList.remove('border-green-500', 'focus:border-green-500', 'border-2');
                // Se agrega un color rojo al input
                document.querySelector(`input[name='REGISTRO_${$inputName}']`).classList.add('border-red-500', 'focus:border-red-500', 'border-2');
                inputLleno[$inputName] = false;
            }
        }
    
    }
    
    const validarFormulario = evento => {
        switch (evento.target.name) {
            case 'REGISTRO_RUT':
                validarCampo(evento, expresiones.run)
                break;
    
            case 'REGISTRO_FECHA':
                validarCampo(evento, expresiones.fecha)
                break;
    
            case 'REGISTRO_NOMBRE':
                validarCampo(evento, expresiones.texto)
                break;
    
            case 'REGISTRO_PATERNO':
                validarCampo(evento, expresiones.texto)
                break;
    
            case 'REGISTRO_MATERNO':
                validarCampo(evento, expresiones.texto)
                break;
    
            case 'REGISTRO_CORREO':
                validarCampo(evento, expresiones.email)
                break;
    
            case 'REGISTRO_CELULAR':
                validarCampo(evento, expresiones.numero)
                break;
    
            case 'REGISTRO_DIRECCION':
                validarCampo(evento, expresiones.direccion)
                break;
    
            case 'REGISTRO_CONTRASENIA1':
                validarCampo(evento, expresiones.contrasenia)
                break;
    
            case 'REGISTRO_CONTRASENIA2':
                validarCampo(evento, expresiones.contrasenia)
                break;
            }
    
        $selects.forEach( select => {
            select.options.selectedIndex !== 0 ? inputLleno.region = true : inputLleno.region = false;
            select.options.selectedIndex !== 0 ? inputLleno.provincia = true : inputLleno.provincia = false;
            select.options.selectedIndex !== 0 ? inputLleno.comuna = true : inputLleno.comuna = false;
        });
    
    };
    
    $inputs.forEach( input => {
        //input.addEventListener('keyup', validarFormulario);
        input.addEventListener('blur', validarFormulario);
    });
    
    $formulario.addEventListener('submit', evento => {
        evento.preventDefault(); // Evita que el formulario se envie si no se encuentra completo.
    
        if (inputLleno.rut === true && inputLleno.fecha === true && inputLleno.nombre === true && inputLleno.paterno === true && inputLleno.materno === true &&
            inputLleno.correo === true && inputLleno.celular === true && inputLleno.direccion === true && inputLleno.contrasenia1 === true &&
            inputLleno.contrasenia2 === true && inputLleno.region === true && inputLleno.provincia === true && inputLleno.comuna === true) {
            document.querySelector('.contenedor-formulario-incompleto').classList.remove('block');
            $formulario.submit();
            // $formulario.reset();
            // setTimeout(() => {
            //     location.href = "{% url 'login' %}"
            // }, 5000);
        } else {
            document.querySelector('.contenedor-formulario-completo').classList.remove('block');
            document.querySelector('.contenedor-formulario-incompleto').classList.add('block');
            setTimeout(() => document.querySelector('.contenedor-formulario-incompleto').classList.remove('block'), 5000);
        }
    
    });
    
    
    if(parseInt(mensajeRegistro, 10) === 2){
        document.querySelector('.contenedor-formulario-completo').classList.add('block');
        setTimeout(() => document.querySelector('.contenedor-formulario-completo').classList.remove('block'), 5000);
        $formulario.reset();
        setTimeout(() => location.href = "http://127.0.0.1:8000/login/", 5000);
    };
};