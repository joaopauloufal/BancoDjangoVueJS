<template>
  <div>
    <breadcrumb>
      <li><nuxt-link to="/bancos">Bancos</nuxt-link></li>
      <li class="is-active"><a href="#" aria-current="page">Criar novo banco</a></li>
    </breadcrumb>
    <div class="columns">
      <div class="column is-6">
        <form-banco v-model="formData" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import Breadcrumb from '~/components/base_components/Breadcrumb.vue'
import FormBanco from '~/components/page_components/FormBanco.vue'
import Banco from '~/types/Banco'

@Component({
  components: {
    Breadcrumb, FormBanco
  }
})
export default class BancosCreate extends Vue {

  formData: Banco = {
    codigo_banco: '',
    nome: ''
  }

  submit ():void {
    window.console.log(this.formData)
  }

}

</script>
