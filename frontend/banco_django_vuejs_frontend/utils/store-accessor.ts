import { Store } from 'vuex'
import { getModule } from 'vuex-module-decorators'
import BancoModule from '~/store/bancos'

let bancos: BancoModule

function initialiseStores(store: Store<any>): void {
  bancos = getModule(BancoModule, store)
}

export { initialiseStores, bancos }
