<template>
    <div class="col-12">
        <div class="row">
            <div class="position-relative pt-5">
                <div class="position-absolute top-200 start-50 translate-middle mt-5">
                    <table class="table table-bordered mt-5 container">
                        <tbody class="table-group-divider mt-5">
                            <tr class="output">
                                <td class="number-container" colspan="4">
                                    {{ output }}
                                </td>
                            </tr>
                            <tr>
                                <td class="p-4 cursor-pointer" v-on:click="clearField">Del</td>
                                <td class="p-4 cursor-pointer" v-on:click="setNegativeOrPositive">
                                    <svg 
                                        xmlns="http://www.w3.org/2000/svg" 
                                        width="1em" 
                                        height="1em" 
                                        viewBox="0 0 24 24"
                                    >
                                        <path 
                                            fill="currentColor" 
                                            d="M12 7.998H8v4H6v-4H2v-2h4v-4h2v4h4zm10 10h-8v-2h8zM18.5 4L4 18.5L5.5 20L20 5.5z"
                                        >
                                        </path>
                                    </svg>
                                </td>
                                <td class="p-4 cursor-pointer" v-on:click="calculatePercentage">
                                    <svg 
                                        xmlns="http://www.w3.org/2000/svg" 
                                        width="1em" 
                                        height="1em" 
                                        viewBox="0 0 24 24"
                                    >
                                        <path 
                                            fill="currentColor" 
                                            d="M7.5 4C5.57 4 4 5.57 4 7.5S5.57 11 7.5 11S11 9.43 11 7.5S9.43 4 7.5 4zm0 5C6.67 9 6 8.33 6 7.5S6.67 6 7.5 6S9 6.67 9 7.5S8.33 9 7.5 9zm9 4c-1.93 0-3.5 1.57-3.5 3.5s1.57 3.5 3.5 3.5s3.5-1.57 3.5-3.5s-1.57-3.5-3.5-3.5zm0 5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5s1.5.67 1.5 1.5s-.67 1.5-1.5 1.5zM5.41 20L4 18.59L18.59 4L20 5.41L5.41 20z">
                                        </path>
                                    </svg>
                                </td>
                                <td class="p-3 cursor-pointer" v-on:click="processOutput('divide')">
                                    <svg 
                                        xmlns="http://www.w3.org/2000/svg" 
                                        width="1em" 
                                        height="1em" 
                                        viewBox="0 0 24 24"
                                    >
                                        <path 
                                            fill="currentColor" 
                                            d="M14 7a2 2 0 1 1-4 0a2 2 0 0 1 4 0ZM3 12a1 1 0 0 1 1-1h16a1 1 0 1 1 0 2H4a1 1 0 0 1-1-1Zm9 7a2 2 0 1 0 0-4a2 2 0 0 0 0 4Z"
                                        >
                                        </path>
                                    </svg>
                                </td>
                            </tr>
                            <tr>
                                <td class="p-4 cursor-pointer" v-on:click="getNumber('7')">7</td>
                                <td class="p-4 cursor-pointer" v-on:click="getNumber('8')">8</td>
                                <td class="p-4 cursor-pointer" v-on:click="getNumber('9')">9</td>
                                <td class="p-4 cursor-pointer" v-on:click="processOutput('multiply')">
                                    <svg 
                                        xmlns="http://www.w3.org/2000/svg" 
                                        width="1em" height="1em" 
                                        viewBox="0 0 20 20"
                                    >
                                        <path 
                                            fill="currentColor" 
                                            fillRule="evenodd" 
                                            d="M4.293 4.293a1 1 0 0 1 1.414 0L10 8.586l4.293-4.293a1 1 0 1 1 1.414 1.414L11.414 10l4.293 4.293a1 1 0 0 1-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 0 1-1.414-1.414L8.586 10L4.293 5.707a1 1 0 0 1 0-1.414Z" 
                                            clipRule="evenodd"
                                        >
                                        </path>
                                    </svg>
                            </td>
                            </tr>
                            <tr>
                                <td class="p-4 cursor-pointer" v-on:click="getNumber('4')">4</td>
                                <td class="p-4 cursor-pointer" v-on:click="getNumber('5')">5</td>
                                <td class="p-4 cursor-pointer" v-on:click="getNumber('6')">6</td>
                                <td class="p-4 cursor-pointer" v-on:click="processOutput('subtract')">
                                    <svg 
                                        xmlns="http://www.w3.org/2000/svg" 
                                        width="1em" 
                                        height="1em" 
                                        viewBox="0 0 1024 1024"
                                    >
                                        <path 
                                            fill="currentColor" 
                                            d="M128 544h768a32 32 0 1 0 0-64H128a32 32 0 0 0 0 64z"
                                        >
                                        </path>
                                    </svg>
                                </td>
                            </tr>
                            <tr>
                            <td class="p-4 cursor-pointer" v-on:click="getNumber('1')">1</td>
                            <td class="p-4 cursor-pointer" v-on:click="getNumber('2')">2</td>
                            <td class="p-4 cursor-pointer" v-on:click="getNumber('3')">3</td>
                            <td class="p-4 cursor-pointer" v-on:click="processOutput('add')">
                                <svg 
                                    xmlns="http://www.w3.org/2000/svg" 
                                    width="1em" 
                                    height="1em" 
                                    viewBox="0 0 1024 1024"
                                >
                                    <path 
                                        fill="currentColor"
                                        d="M480 480V128a32 32 0 0 1 64 0v352h352a32 32 0 1 1 0 64H544v352a32 32 0 1 1-64 0V544H128a32 32 0 0 1 0-64h352z"
                                    >
                                    </path>
                                </svg>
                            </td>
                            </tr>
                            <tr>
                            <td class="p-4 cursor-pointer" v-on:click="getDot()">.</td>
                            <td class="p-4 cursor-pointer" colspan="2" v-on:click="getNumber('0')">
                               0
                            </td>
                            <td class="p-4 cursor-pointer" v-on:click="updateOutput()">
                                =
                            </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  export default {
    name: [
        'EpMinus', 
        'EpPlus', 
        'HeroiconsSolidX', 
        'FaSolidDivide', 
        'FaSolidPercentage',
        'IcOutlinePercent', 
        'IcBaselinePlusMinusAlt',
        'GgMathDivide'
    ],
    data(){
        return {
            output: '',
            previousValue: null,
            operationFired: false,
        }
    },
    methods: {
        clearField() {
            this.output = '';
        },
        setNegativeOrPositive() {
            this.output = this.output[0] === '-' ? this.output.slice(1) : `-${this.output}`;
        },
        calculatePercentage() {
            this.output = parseFloat(this.output)/100;
        },
        getNumber(number) {
            if (this.operationFired) {
                this.output = '';
                this.operationFired = false;
            }

            this.output = `${this.output}${number}`
        },
        getDot() {
            if (this.output.indexOf('.') === -1) {
                this.output = this.output+'.'
            }
        },
        processOutput(string) {
            if (string == 'add') {
                this.operation = (a, b) => {
                    return parseFloat(a) + parseFloat(b)
                }
            } else if (string == 'subtract') {
                this.operation = (a, b) => {
                    return parseFloat(a) - parseFloat(b)
                }
            } else if (string == 'divide') {
                this.operation = (a, b) => {
                    return parseFloat(a) / parseFloat(b)
                }
            } else if (string == 'multiply') {
                this.operation = (a, b) => {
                    return parseFloat(a) * parseFloat(b)
                }
            }
         
            this.previousValue = this.output;
            this.operationFired = true      
        },
        updateOutput() {
            this.output = `${this.operation(this.previousValue, this.output)}`;
            this.previousValue = null;
        }
    }
  }
</script>  

<style scoped>
.container {
    box-shadow: 2px 2px 2px 1px rgba(0, 0, 0, 0.2);
}

.output {
    background-color: aquamarine;
    color: black;
}

.cursor-pointer {
    cursor: pointer;
}

.number-container {
    width: 100%;
    height: 80px;
    padding: 10px;
}
</style>