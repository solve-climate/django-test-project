from fasthtml.common import *
from fasthtml.svg import Path, Rect, G, Polyline, Line

custom_theme = Style("""
:root {
  default: true;
  --color-base-100: oklch(14% 0.004 49.25);
  --color-base-200: oklch(21% 0.006 56.043);
  --color-base-300: oklch(26% 0.007 34.298);
  --color-base-content: oklch(97% 0.001 106.424);
    --color-base-100: oklch(22% 0.019 237.69);
  --color-base-200: oklch(20% 0.019 237.69);
  --color-base-300: oklch(18% 0.019 237.69);
  --color-base-content: oklch(77.383% 0.043 245.096);
  --color-primary: oklch(74.703% 0.158 39.947);
  --color-primary-content: oklch(14.94% 0.031 39.947);
  --color-secondary: oklch(72.537% 0.177 2.72);
  --color-secondary-content: oklch(14.507% 0.035 2.72);
  --color-accent: oklch(71.294% 0.166 299.844);
  --color-accent-content: oklch(14.258% 0.033 299.844);
  --color-neutral: oklch(26% 0.019 237.69);
  --color-neutral-content: oklch(70% 0.019 237.69);
  --color-info: oklch(85.559% 0.085 206.015);
  --color-info-content: oklch(17.111% 0.017 206.015);
  --color-success: oklch(85.56% 0.085 144.778);
  --color-success-content: oklch(17.112% 0.017 144.778);
  --color-warning: oklch(85.569% 0.084 74.427);
  --color-warning-content: oklch(17.113% 0.016 74.427);
  --color-error: oklch(85.511% 0.078 16.886);
  --color-error-content: oklch(17.102% 0.015 16.886);
  --radius-selector: 1rem;
  --radius-field: 0.5rem;
  --radius-box: 1rem;
  --size-selector: 0.25rem;
  --size-field: 0.25rem;
  --border: 1px;
  --depth: 0;
  --noise: 0;
}
""")

daisy_hdrs = (
    Link(href='https://cdn.jsdelivr.net/npm/daisyui@5', rel='stylesheet', type='text/css'),
    Script(src='https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4'),
    custom_theme
)

app = FastHTML(hdrs=daisy_hdrs)
rt = app.route

icon = Svg(cls='w-1/4 lucide lucide-lightbulb lg:block hidden', xmlns='http://www.w3.org/2000/svg', viewbox='0 0 24 24', fill='none', stroke='currentColor', stroke_width='2', stroke_linecap='round', stroke_linejoin='round')(
    Path(d='M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5'),
    Path(d='M9 18h6'),
    Path(d='M10 22h4')
)

iconSlack = Svg(cls='w-1/4 lucide lucide-slack lg:block hidden', xmlns='http://www.w3.org/2000/svg', viewbox='0 0 24 24', fill='none', stroke='currentColor', stroke_width='2', stroke_linecap='round', stroke_linejoin='round')(
    Rect(width='3', height='8', x='13', y='2', rx='1.5'),
    Path(d='M19 8.5V10h1.5A1.5 1.5 0 1 0 19 8.5'),
    Rect(width='3', height='8', x='8', y='14', rx='1.5'),
    Path(d='M5 15.5V14H3.5A1.5 1.5 0 1 0 5 15.5'),
    Rect(width='8', height='3', x='14', y='13', rx='1.5'),
    Path(d='M15.5 19H14v1.5a1.5 1.5 0 1 0 1.5-1.5'),
    Rect(width='8', height='3', x='2', y='8', rx='1.5'),
    Path(d='M8.5 5H10V3.5A1.5 1.5 0 1 0 8.5 5')
)

iconCalender = Svg(cls='w-1/4 lucide lucide-calendar-days lg:block hidden', xmlns='http://www.w3.org/2000/svg', viewbox='0 0 24 24', fill='none', stroke='currentColor', stroke_width='2', stroke_linecap='round', stroke_linejoin='round')(
    Path(d='M8 2v4'), Path(d='M16 2v4'),
    Rect(width='18', height='18', x='3', y='4', rx='2'),
    Path(d='M3 10h18'), Path(d='M8 14h.01'), Path(d='M12 14h.01'),
    Path(d='M16 14h.01'), Path(d='M8 18h.01'), Path(d='M12 18h.01'), Path(d='M16 18h.01')
)

emailInput = Div(
    Legend('What is your email address?', cls='fieldset-legend'),
    Label(cls='input validator w-full')(
        Svg(xmlns='http://www.w3.org/2000/svg', viewbox='0 0 24 24', cls='h-[1em] opacity-50')(
            G(stroke_linejoin='round', stroke_linecap='round', stroke_width='2.5', fill='none', stroke='currentColor')(
                Rect(width='20', height='16', x='2', y='4', rx='2'),
                Path(d='m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7')
            )
        ),
        Input(type='email', placeholder='mail@site.com', required='')
    ),
    Div('Enter valid email address', cls='validator-hint hidden')
)

textArea = Div(
    Legend('What do you want to tell us?', cls='fieldset-legend'),
    Textarea(placeholder='message', cls='textarea h-50 w-full'),
)

hero = Div(cls='hero bg-base-200 min-h-screen')(
    Div(cls='hero-content text-center')(
        Div(cls='max-w-md')(
            H1('Hi, Welcome to the home of Solve Climate', cls='text-5xl font-bold'),
            P('Are you ready to work on solutions with others to make the world a better place?', cls='py-6'),
            Button('Get Started', cls='btn btn-primary')
        )
    )
)

hero2 = Div(cls='hero bg-base-800 min-h-screen')(
    Div(cls='hero-content flex-col lg:flex-row lg:justify-around min-w-4/5 lg:min-w-3/5')(
        icon,
        Div(cls='max-w-md')(
            H1('The idea', cls='text-5xl font-bold'),
            P('Your idea text here...', cls='py-6')
        )
    )
)

hero3 = Div(cls='hero bg-base-200 min-h-screen')(
    Div(cls='hero-content flex-col lg:flex-row lg:justify-around min-w-4/5 lg:min-w-3/5')(
        Div(cls='max-w-md')(
            H1('The platform we use', cls='text-5xl font-bold'),
            P('Your platform text here...', cls='py-6'),
            Button('Join the slack channel', cls='btn btn-primary')
        ),
        iconSlack
    )
)

hero4 = Div(cls='hero bg-base-800 min-h-screen')(
    Div(cls='hero-content flex-col lg:flex-row lg:justify-around min-w-4/5 lg:min-w-3/5')(
        iconCalender,
        Div(cls='max-w-md')(
            H1('When is the next solvaton?', cls='text-5xl font-bold'),
            P('The first week of March', cls='py-6'),
        )
    )
)

hero5 = Div(cls='hero bg-base-200 min-h-screen')(
    Div(cls='hero-content flex-col lg:flex-row lg:justify-around min-w-4/5 lg:min-w-3/5')(
        Div(cls='max-w-md flex flex-col gap-6')(
            H1('We like to hear from you!', cls='text-5xl font-bold'),
            P('If you have questions, leave us a message below'),
            emailInput,
            textArea,
            Button('Send', cls='btn btn-primary w-full')
        ),
        iconCalender
    )
)

@rt('/')
def home(): return Div(hero, hero2, hero3, hero4, hero5)

serve()