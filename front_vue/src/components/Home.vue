<template>
  <div class="">
      <p>{{ mensaje }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Main',
    data () {
        return {
            mensaje: 'Hola desde Vue'
        }
    },
    methods: {
        getMensaje () {
            const path = 'http://127.0.0.1:5000/api/v1.0/mensaje'
            axios.get(path).then((respuesta) => {
                this.mensaje = respuesta.data
            })
            .catch((error) => {
                console.error(error);
            })
        }
    },
    created(){
        this.getMensaje()
    }
}
</script>

<style>

</style>