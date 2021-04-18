<template>
  <section class="section">
    <div class="columns">
      <div class="column">
        <b-button type="is-primary" class="is-pulled-right" icon-left="plus">Novo Banco</b-button>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <b-table
          :data="bancosList"
          per-page="10"
          paginated
          default-sort="nome"
        >
          <b-table-column label="Código do Banco" field="codigo_banco" v-slot="props" sortable searchable>
            {{ props.row.codigo_banco }}
          </b-table-column>
          <b-table-column label="Nome" field="nome" v-slot="props" sortable searchable>
            {{ props.row.nome }}
          </b-table-column>
          <b-table-column label="Ações">
            <b-button type="is-primary" icon-right="pencil"/>
            <b-button type="is-primary" icon-right="delete"/>
          </b-table-column>
          <template #empty>
            <div class="has-text-centered">Não há bancos cadastrados.</div>
          </template>
        </b-table>
      </div>
    </div>
  </section>
</template>

<script lang="ts">

import { Vue, Component } from 'vue-property-decorator'
import { bancos } from '~/store'
import Banco from '~/types/Banco'

@Component
export default class BancosIndex extends Vue {

  created ():void {
    bancos.getBancos()
  }

  get bancosList ():Banco[] {
    return bancos.bancosList
  }

}

</script>
