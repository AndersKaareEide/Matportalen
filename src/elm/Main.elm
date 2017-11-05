module Main exposing (..)

import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import Types exposing (..)
import JsonDecoder exposing (..)
import Json.Decode exposing (Value)


main : Program Value Model Msg
main =
    programWithFlags { init = init, view = view, update = update, subscriptions = subscriptions }



--flags : Json.Values


subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none


init : Value -> ( Model, Cmd Msg )
init json =
    ( { restaurants = getRestaurantsProper json, currentRestaurant = "", result = testDecoder json }, Cmd.none )


type Msg
    = ViewRestaurant String
    | Home


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        ViewRestaurant name ->
            ( { model | currentRestaurant = name }, Cmd.none )

        Home ->
            ( { model | currentRestaurant = "" }, Cmd.none )


view : Model -> Html Msg
view model =
    div [ class "home" ]
        ([ text model.currentRestaurant
         , button [ onClick (ViewRestaurant "Valeri Kebab") ] [ text "heiasd" ]
         ]
            ++ List.map (\rest -> text rest.name) model.restaurants
        )
