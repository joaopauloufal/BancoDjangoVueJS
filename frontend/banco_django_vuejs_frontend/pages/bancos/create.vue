<template>
  <div>
    <breadcrumb>
      <li><nuxt-link to="/bancos">Bancos</nuxt-link></li>
      <li class="is-active"><a href="#" aria-current="page">Criar novo banco</a></li>
    </breadcrumb>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import Breadcrumb from '~/components/Breadcrumb'

@Component
export default class BancosCreate extends Vue {

}

</script>
