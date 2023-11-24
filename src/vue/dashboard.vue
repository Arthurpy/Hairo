<template>
    <div class="dash">
        <sidebar :activeButton="'dashboard'"/>
        <div class="dashboard">
            <div class="ligne">
            <div class="orange">
                Vos exploits en résumé  !
                <button @onclick="goTofiche"><div class="fiche">ajouter une fiche</div></button>
                <img class="megaphone" src="../assets/megaphone.png">
            </div>
            </div>
            <div class="ligne">
            <div class="vert">
                <p class="gras">
                    Bonjour Doe,
                </p>
                <p class="gras2">
                    Vous avez fournis de très beaux efforts ces derniers temps continuiez ainsi.
                </p>
            </div>
            <div class="ligne">
            </div>
            <resultatqcm :value="43" />
            <resultatqcm :value="56" />
        </div>
            <div class="ligne">
                <div class="last_question">
                    test
                </div>
            </div>
        </div>
        <profil/>
    </div>
</template>

<script>
import sidebar from '../components/sidebar.vue';
import resultatqcm from '../components/resultatqcm.vue';
import profil from '../components/profil.vue';

export default {
    name: 'Dash',
    components: {
        sidebar,
        resultatqcm,
        profil,
    },
    data() {
        return {
            activeButton: 'dashboard',
            isDarkTheme: false,
        };
    },
    methods: {
        goTofiche() {
            this.$router.push('/fiche');
        },
    }
};
</script>

<style>

.last_question {
    width: 225px;
    height: 127px;
    flex-shrink: 0;
    background-color: #B4E1FE80;
    margin: 25px;
    border-radius: 10px;
}

.ligne {
    display: flex;
    justify-content: space-between;
}

.megaphone {
    width: 141.808px;
    height: 141.808px;
    transform: rotate(-9.534deg);
    flex-shrink: 0;
}

.dash {
    display: flex;
    justify-content: space-between;
}

.dashboard {
    width :100%;
    height: 100vh;
    background: #F3F8FF;
    padding-right: 30px;
}

.fiche {
    width: 138px;
    height: 51px;
    font-size: 16px;
    display: flex;
    border-radius: 10px;
    background: #2176FF;
    color: #FFF;
    justify-content: center;
    align-items: center;
}

.orange {
    width: 100%;
    height: 114px;
    border-radius: 8px;
    background: #FCD19C;
    margin-left: 25px;
    padding-left: 22px;
    margin-top: 36px;
    color: #FFF;
    text-align: center;
    font-family: Poppins;
    font-size: 28px;
    font-style: normal;
    line-height: normal;
    font-weight: 700;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.vert {
    width: 384px;
    height: 127px;
    border-radius: 10px;
    background: var(--green, #D2EADA);
    margin-left: 25px;
    margin-top: 25px;
    padding-left: 14px;
    padding-top: 9px;
}

.gras {
    display: flex;
width: 110px;
height: 33px;
flex-direction: column;
color: #F3F8FF;
justify-content: center;
flex-shrink: 0;
color: #252525;
text-align: center;
font-family: Poppins;
font-size: 16px;
font-style: normal;
font-weight: 700;
line-height: normal
}

.gras2{
    display: flex;
    width: 100%;
    height: 33px;
    flex-direction: column;
    color: #F3F8FF;
    justify-content: center;
    flex-shrink: 0;
    color: #252525;
    text-align: center;
    font-family: Poppins;
    font-size: 16px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
}

</style>