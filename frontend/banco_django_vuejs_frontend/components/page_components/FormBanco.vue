<template>
  <div class="card" @input="getFormData">
    <div class="card-header">
      <p class="card-header-title">
        {{titulo}}
      </p>
    </div>
    <div class="card-content">
      <b-field
        label="Código do banco"
        :type="formErrors.codigo_banco ? 'is-danger': ''"
        :message="formErrors.codigo_banco ? formErrors.codigo_banco: ''"
      >
        <b-input v-model="formData.codigo_banco" name="codigo_banco"></b-input>
      </b-field>
      <b-field
        label="Nome"
        :type="formErrors.nome ? 'is-danger': ''"
        :message="formErrors.nome ? formErrors.nome: ''"
      >
        <b-input v-model="formData.nome" name="nome"></b-input>
      </b-field>
    </div>
    <footer class="card-footer is-justify-content-center pt-3 pb-3">
      <div class="buttons">
        <b-button type="is-primary" @click="salvarEvent">Salvar</b-button>
        <b-button @click="cancelarEvent">Cancelar</b-button>
      </div>
    </footer>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Emit, Prop } from 'vue-property-decorator'
import Banco from '~/types/Banco'
import { bancos } from '~/store'

@Component
export default class FormBanco extends Vue {

  $parent!: any

  @Prop({ type: String, required: true, default: ''}) titulo!: string
  @Prop({ required: false }) bancoId!: number

  formData: Banco = {
    id: '',
    codigo_banco: '',
    nome: ''
  }

  mounted () {
    if (this.bancoId !== undefined) {
      this.getBanco(this.bancoId)
    }
  }

  @Emit('input')
  getFormData ():Banco {
    return this.formData
  }

  salvarEvent():void {
    this.$parent.submit()
  }

  cancelarEvent():void {
    bancos.clearErrors()
    this.$router.push('/bancos')
  }

  get formErrors ():any {
    return bancos.errors
  }

  async getBanco (bancoId: number):Promise<void> {
    await bancos.getBanco(bancoId)
    Object.assign(this.formData, bancos.banco)
    this.$emit('input', this.formData)
  }

}

</script>
