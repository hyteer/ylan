import { createStore } from 'redux'
import todoApp from '../reducers'
import { addTodo, toggleTodo, setVisibilityFilter, VisibilityFilters } from '../Actions'
const { SHOW_ALL } = VisibilityFilters
const { SHOW_COMPLETED } = VisibilityFilters

let store = createStore(todoApp)

console.log(SHOW_ALL+SHOW_COMPLETED)



// Log the initial state
console.log("this is tests for todo app...")
console.log(store.getState())

// Every time the state changes, log it
// Note that subscribe() returns a function for unregistering the listener
let unsubscribe = store.subscribe(() =>
  console.log(store.getState())
)

// Dispatch some actions
store.dispatch(addTodo('Learn about actions'))
store.dispatch(addTodo('Learn about reducers'))
store.dispatch(addTodo('Learn about store'))
store.dispatch(toggleTodo(0))
store.dispatch(toggleTodo(1))
store.dispatch(setVisibilityFilter(VisibilityFilters.SHOW_COMPLETED))

// Stop listening to state updates
unsubscribe()
