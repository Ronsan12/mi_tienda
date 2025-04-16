/* globo carrito */
document.addEventListener('DOMContentLoaded', function() {
    actualizarContadorCarrito();
});

function actualizarContadorCarrito() {
    fetch('/obtener_cantidad_carrito/')
        .then(response => response.json())
        .then(data => {
            const contadorCarrito = document.getElementById('contador-carrito');
            if (contadorCarrito) {
                contadorCarrito.textContent = data.total;
            }
        })
        .catch(error => console.error('Error al actualizar contador del carrito:', error));
}

setInterval(actualizarContadorCarrito, 30000); // Actualiza cada 30 segundos

/* Filtro desplegable */
document.addEventListener('DOMContentLoaded', function() {
    var filtroTamaño = document.getElementById('filtro-tamaño');
    if (filtroTamaño) {
        filtroTamaño.addEventListener('change', function() {
            const tamañoSeleccionado = this.value;
            const urlParams = new URLSearchParams(window.location.search);
            if (tamañoSeleccionado) {
                urlParams.set('tamaño', tamañoSeleccionado);
            } else {
                urlParams.delete('tamaño');
            }
            window.location.search = urlParams.toString();
        });
    }
});