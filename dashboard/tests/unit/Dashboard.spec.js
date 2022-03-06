import { shallowMount } from '@vue/test-utils'
import Dashboard from '@/components/Dashboard.vue'

describe('Dashboard component test', () =>{
   it ('create component',()=>{
        const wrapper = shallowMount(Dashboard)

        expect(wrapper.vm.$data.stompEndpoint).toEqual('ws://localhost:61613')
   })
})
