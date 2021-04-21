<template>
  <div class="card" @input="getFormData">
    <div class="card-header">
      <p class="card-header-title">
        Criar novo banco
      </p>
    </div>
    <div class="card-content">
      <b-field label="Código do banco">
        <b-input v-model="banco.codigo_banco" name="codigo_banco"></b-input>
      </b-field>
      <b-field label="Nome">
        <b-input v-model="banco.nome" name="nome"></b-input>
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
import { Vue, Component, Emit } from 'vue-property-decorator'
import Banco from '~/types/Banco'

@Component
export default class FormBanco extends Vue {

  banco: Banco = {
    codigo_banco: '',
    nome: ''
  }

  @Emit('input')
  getFormData ():Banco {
    return this.banco
  }

  salvarEvent():void {
    this.$parent.submit()
  }

  cancelarEvent():void {
    this.$router.push('/bancos')
  }

}

</script>
