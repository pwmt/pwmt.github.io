{-# LANGUAGE OverloadedStrings #-}
module Main where

import Prelude hiding (id)
import Control.Category (id)
import Control.Arrow ((>>>), (***), arr)
import Data.Monoid (mempty, mconcat)
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

  match "css/fonts/**" $ do
    route idRoute
    compile copyFileCompiler

  match "img/*" $ do
    route idRoute
    compile copyFileCompiler

  match "templates/*" $ do
    compile templateCompiler

  -- index --
  match  "index.html" $ route idRoute
  create "index.html" $ constA mempty
    >>> arr (setField "title" "Home")
    >>> arr (setField "sidebar" "")
    >>> requireAllA "news/*" (id *** arr (take 3 . reverse . chronological) >>> addPostList)
    >>> setFieldPage "home" "content/home.md"
    >>> applyTemplateCompiler "templates/index.html"
    >>> applyTemplateCompiler "templates/home.html"
    >>> applyTemplateCompiler "templates/default.html"
    >>> relativizeUrlsCompiler

  -- news --
  match  "news/index.html" $ route idRoute
  create "news/index.html" $ constA mempty
    >>> arr (setField "title" "News")
    >>> arr (setField "description" "Anything new?")
    >>> arr (setField "sidebar" "")
    >>> requireAllA "news/*.md" addPostList
    >>> applyTemplateCompiler "templates/news.html"
    >>> applyTemplateCompiler "templates/page.html"
    >>> applyTemplateCompiler "templates/default.html"
    >>> relativizeUrlsCompiler

  match "news/*.md" $ do
    route $ cleanURL
    compile $ pageCompiler
      >>> arr (setField "sidebar" "")
      >>> applyTemplateCompiler "templates/news-post.html"
      >>> applyTemplateCompiler "templates/page.html"
      >>> applyTemplateCompiler "templates/default.html"
      >>> relativizeUrlsCompiler

  -- content --
  match "sidebar/*.md" $ do
    compile $ pageCompiler

  match "content/home.md" $ do
    compile $ pageCompiler

  match "content/projects/zathura**.md" $ do
    route $ setRoot `composeRoutes` cleanURL
    compile $ pageCompiler
      >>> setFieldPage "sidebar" "sidebar/zathura.md"
      >>> applyTemplateCompiler "templates/page.html"
      >>> applyTemplateCompiler "templates/default.html"
      >>> relativizeUrlsCompiler

  match "content/projects/girara**.md" $ do
    route $ setRoot `composeRoutes` cleanURL
    compile $ pageCompiler
      >>> setFieldPage "sidebar" "sidebar/girara.md"
      >>> applyTemplateCompiler "templates/page.html"
      >>> applyTemplateCompiler "templates/default.html"
      >>> relativizeUrlsCompiler

  match "content/projects/jumanji**.md" $ do
    route $ setRoot `composeRoutes` cleanURL
    compile $ pageCompiler
      >>> setFieldPage "sidebar" "sidebar/jumanji.md"
      >>> applyTemplateCompiler "templates/page.html"
      >>> applyTemplateCompiler "templates/default.html"
      >>> relativizeUrlsCompiler

  match "content/projects.md" $ do
    route $ setRoot `composeRoutes` cleanURL
    compile $ pageCompiler
      >>> arr (setField "sidebar" "")
      >>> applyTemplateCompiler "templates/page.html"
      >>> applyTemplateCompiler "templates/default.html"
      >>> relativizeUrlsCompiler

  match "content/**.md" $ do
    route $ setRoot `composeRoutes` cleanURL
    compile $ pageCompiler
      >>> arr (setField "sidebar" "")
      >>> applyTemplateCompiler "templates/page.html"
      >>> applyTemplateCompiler "templates/default.html"
      >>> relativizeUrlsCompiler

  match "content/**" $ do
    route $ setRoot
    compile copyFileCompiler

  match "404.html" $ do
    route idRoute
    compile $ pageCompiler
      >>> arr (setField "sidebar" "")
      >>> applyTemplateCompiler "templates/page.html"
      >>> applyTemplateCompiler "templates/default.html"

  -- newsfeed --
  match  "rss.xml" $ route idRoute
  create "rss.xml" $ requireAll_ "news/*.md" >>> renderRss feedConfiguration

  match  "atom.xml" $ route idRoute
  create "atom.xml" $ requireAll_ "news/*.md" >>> renderAtom feedConfiguration

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

addPostList :: Compiler (Page String, [Page String]) (Page String)
addPostList = setFieldA "news" $
  arr (reverse . chronological)
    >>> require "templates/news-item.html" (\p t -> map (applyTemplate t) p)
    >>> arr mconcat
    >>> arr pageBody
