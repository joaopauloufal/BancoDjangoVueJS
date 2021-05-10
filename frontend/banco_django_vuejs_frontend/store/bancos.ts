import { Module, VuexModule, Mutation, Action } from 'vuex-module-decorators'
import Banco from '~/types/Banco'
import { $axios } from '~/utils/api'

@Module({
  name: 'bancos',
  stateFactory: true,
  namespaced: true,
})
export default class BancoModule extends VuexModule {
  bancosList: Banco[] = []
  banco: Banco = {
    id: '', codigo_banco: '', nome: ''
  }
  errors: any[] = []

  @Mutation
  setBancos(bancos: Banco[]):void {
    this.bancosList = bancos
  }

  @Mutation
  setBanco(banco: Banco):void {
    this.banco = banco
  }

  @Mutation
  setErrors(errors: any[]):void {
    this.errors = errors
  }

  @Mutation
  clearErrors():void {
    this.errors = []
  }

  @Action({ commit: 'setBancos' })
  async getBancos():Promise<void> {
    return $axios.$get('bancos/')
  }

  @Action({rawError:true, commit: 'setBanco' })
  async getBanco(bancoId:number):Promise<void> {
    return $axios.$get(`bancos/${bancoId}/`)
  }

  @Action({rawError:true})
  addBanco(banco:Banco) {
    return $axios.$post('bancos/', banco)
  }

  @Action({rawError:true})
  async updateBanco(banco:Banco) {
    return $axios.$put(`bancos/${banco.id}/`, banco)
  }

  @Action({rawError:true})
  async deleteBanco(id:string) {
    return $axios.$delete(`bancos/${id}/`)
  }

}
