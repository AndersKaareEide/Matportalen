module Types exposing (..)


type alias Model =
    { restaurants : List Restaurant
    , currentRestaurant : String
    , result : Result String (List Visit)
    }


type alias Restaurant =
    { name : String
    , orgnr : String
    , visits : List Visit
    }


type alias Visit =
    { date : String
    , orgnr : String
    , grade : String
    , name : String
    }
