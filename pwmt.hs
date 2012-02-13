{-# LANGUAGE OverloadedStrings #-}
module Main where

import Control.Arrow ((>>>), arr)
import Data.Monoid (mempty)
import System.FilePath

import Hakyll

main::IO()
main = hakyll $ do
  -- basic --
  match "css/*" $ do
    route $ setExtension "css"
    compile $ byExtension (error "Invalid file")
      [ (".css", compressCssCompiler)
      , (".styl", stylusCompiler)
      ]

  match "img/*" $ do
    route idRoute
    compile copyFileCompiler

  match "templates/*" $ do
    compile templateCompiler

  -- index --
  match  "index.html" $ route idRoute
  create "index.html" $ constA mempty
    >>> arr (setField "title" "home")
    >>> setFieldPage "home" "content/home.md"
    >>> applyTemplateCompiler "templates/index.html"
    >>> applyTemplateCompiler "templates/default.html"
    >>> relativizeUrlsCompiler

  -- news --
  match  "news/index.html" $ route idRoute
  create "news/index.html" $ constA mempty
    >>> applyTemplateCompiler "templates/news.html"
    >>> applyTemplateCompiler "templates/default.html"
    >>> relativizeUrlsCompiler

  match "news/*" $ do
    route $ cleanURL
    compile $ pageCompiler
      >>> applyTemplateCompiler "templates/news-post.html"
      >>> applyTemplateCompiler "templates/default.html"
      >>> relativizeUrlsCompiler

  -- content --
  match "content/home.md" $ do
    compile $ pageCompiler

  match "content/projects/zathura**" $ do
    route $ setRoot `composeRoutes` cleanURL
    compile $ pageCompiler
      >>> applyTemplateCompiler "templates/page.html"
      >>> applyTemplateCompiler "templates/zathura-menu.html"
      >>> applyTemplateCompiler "templates/default.html"
      >>> relativizeUrlsCompiler

  match "content/**" $ do
    route $ setRoot `composeRoutes` cleanURL
    compile $ pageCompiler
      >>> applyTemplateCompiler "templates/page.html"
      >>> applyTemplateCompiler "templates/default.html"
      >>> relativizeUrlsCompiler

  -- newsfeed --
  match  "rss.xml" $ route idRoute
  create "rss.xml" $ requireAll_ "news/*" >>> renderRss feedConfiguration

  match  "atom.xml" $ route idRoute
  create "atom.xml" $ requireAll_ "news/*" >>> renderAtom feedConfiguration

-- rss --
feedConfiguration :: FeedConfiguration
feedConfiguration = FeedConfiguration
  { feedTitle       = "pwmt.org - news feed"
  , feedDescription = "programs with movie titles"
  , feedAuthorName  = "pwmt.org"
  , feedRoot        = "http://pwmt.org"
  }

-- functions --
setRoot :: Routes
setRoot = customRoute stripTopDir

stripTopDir :: Identifier() -> FilePath
stripTopDir = joinPath . tail . splitPath . toFilePath

cleanURL :: Routes
cleanURL = customRoute fileToDirectory

fileToDirectory :: Identifier() -> FilePath
fileToDirectory = (flip combine) "index.html" . dropExtension . toFilePath

stylusCompiler :: Compiler Resource String
stylusCompiler = getResourceString >>> unixFilter "stylus" ["-c"]
