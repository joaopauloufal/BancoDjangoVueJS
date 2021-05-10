<template>
  <div>
    <breadcrumb>
      <li><nuxt-link to="/bancos">Bancos</nuxt-link></li>
      <li class="is-active"><a href="#" aria-current="page">Criar novo banco</a></li>
    </breadcrumb>
    <div class="columns">
      <div class="column is-6">
        <form-banco v-model="formData" titulo="Criar novo banco" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import Breadcrumb from '~/components/base_components/Breadcrumb.vue'
import FormBanco from '~/components/page_components/FormBanco.vue'
import Banco from '~/types/Banco'
import { bancos } from '~/store'
import { ToastProgrammatic as Toast } from 'buefy'

@Component({
  components: {
    Breadcrumb, FormBanco
  }
})
export default class BancosCreate extends Vue {

  formData: Banco = {
    id: '',
    codigo_banco: '',
    nome: ''
  }

  async submit ():Promise<void> {
    await bancos.addBanco(this.formData).then(() => {
      Toast.open(
        {
          message: 'Banco criado com sucesso!',
          type: 'is-success',
          duration: 4000
        }
      )
      this.$router.push('/bancos')
    }).catch((error) => {
      if (error.response.status === 400) {
        bancos.setErrors(error.response.data)
      }
    })
  }

}

</script>
